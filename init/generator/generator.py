#!/usr/bin/python3
import copy
import os
import yaml
import sys
from pathlib import Path
from graphlib import TopologicalSorter
from models import models

def process_var_files(directory):
    """Read all YAML files in the directory and combine their 'items' arrays."""
    combined_items = []
    
    if not directory:
        return combined_items
        
    for file_path in Path(directory).glob('*.yaml'):
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
            if data and 'items' in data:
                combined_items.extend(data['items'])
                
    return combined_items

def process_device_type_files(directory):
    """Process device type files and prepare them for Ansible."""
    items = []
    
    if not directory:
        return items
        
    for file_path in Path(directory).glob('*.yaml'):
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
            
            # Create a copy of data and remove the components we'll process separately
            device_type_data = data.copy()
            device_type_data.pop('console-ports', None)
            device_type_data.pop('interfaces', None)
            device_type_data.pop('power-ports', None)
            device_type_data.pop('module-bays', None)
            
            # Add device type with all remaining attributes
            items.append({
                'model': 'device_type',
                'state': 'present',
                'data': device_type_data
            })
            
            # Process console ports
            if 'console-ports' in data:
                for port in data['console-ports']:
                    console_port_data = {
                        'device_type': data['slug'],
                        'name': port['name'],
                        'type': port['type']
                    }
                    
                    items.append({
                        'model': 'console_port_template',
                        'state': 'present',
                        'data': console_port_data
                    })
            
            # Process interfaces - include all supported attributes
            if 'interfaces' in data:
                for interface in data['interfaces']:
                    interface_data = {
                        'device_type': data['slug'],
                        'name': interface['name'],
                        'type': interface['type']
                    }
                    
                    # Include optional attributes if they exist
                    if 'mgmt_only' in interface:
                        interface_data['mgmt_only'] = interface['mgmt_only']
                    if 'poe_mode' in interface:
                        interface_data['poe_mode'] = interface['poe_mode']
                    if 'poe_type' in interface:
                        interface_data['poe_type'] = interface['poe_type']
                    
                    items.append({
                        'model': 'device_interface_template',
                        'state': 'present',
                        'data': interface_data
                    })
            
            # Process power ports - include all supported attributes
            if 'power-ports' in data:
                for port in data['power-ports']:
                    power_port_data = {
                        'device_type': data['slug'],
                        'name': port['name'],
                        'type': port['type']
                    }
                    
                    # Include optional attributes if they exist
                    if 'allocated_draw' in port:
                        power_port_data['allocated_draw'] = port['allocated_draw']
                    if 'maximum_draw' in port:
                        power_port_data['maximum_draw'] = port['maximum_draw']
                    
                    items.append({
                        'model': 'power_port_template',
                        'state': 'present',
                        'data': power_port_data
                    })
                    
            # Process module bays
            if 'module-bays' in data:
                for bay in data['module-bays']:
                    module_bay_data = {
                        'device_type': data['slug'],
                        'name': bay['name']
                    }
                    
                    # Include position if it exists
                    if 'position' in bay:
                        module_bay_data['position'] = bay['position']
                    
                    items.append({
                        'model': 'module_bay_template',
                        'state': 'present',
                        'data': module_bay_data
                    })
    
    return items

def main():
    # Get directory paths from environment variables
    var_files_dir = os.getenv('VAR_FILES_DIR')

    if not var_files_dir:
        print("ERROR: VAR_FILES_DIR environment variable not set", file=sys.stderr)
        sys.exit(1)

    device_type_files_dir = os.getenv('DEVICE_TYPE_FILES_DIR')

    if not device_type_files_dir:
        print("ERROR: DEVICE_TYPE_FILES_DIR environment variable not set", file=sys.stderr)
        sys.exit(1)

    # Process both types of files
    var_items = process_var_files(var_files_dir)
    device_type_items = process_device_type_files(device_type_files_dir)
    
    # Combine all items
    all_items = []
    all_items.extend(var_items)
    all_items.extend(device_type_items)

    # Group items by model
    items_by_model = {}
    for item in all_items:
        model = item['model']
        if model not in items_by_model:
            items_by_model[model] = []
        items_by_model[model].append(item)

    # Build dependency graph for topological sort
    graph = {}
    for model in models:
        graph[model] = set()
        for dep in models[model]['dependencies']:
            if dep in models:  # Only include dependencies that are actual models
                graph[model].add(dep)

    # Get topologically sorted models
    ts = TopologicalSorter(graph)
    sorted_models = list(ts.static_order())

    # Filter to only include models that have items
    sorted_models = [model for model in sorted_models if model in items_by_model]

    # Generate playbook tasks
    tasks = []

    # First run: Create/update items in dependency order
    for model in sorted_models:
        tasks.append({
            'name': f'[{model}] Create/update items',
            f'netbox.netbox.netbox_{model}': {
                'netbox_url': '{{ netbox_url }}',
                'netbox_token': '{{ netbox_token }}',
                'state': '{{ item.state }}',
                'data': '{{ item.data }}'
            },
            'loop': [item for item in copy.deepcopy(items_by_model[model]) if item.get('state') == 'present'],
            'ignore_errors': True,
            'tags': [model, models[model].get('object_type')]
        })

    # Second run: Remove items in reverse dependency order
    for model in reversed(sorted_models):
        tasks.append({
            'name': f'[{model}] Remove items set to absent',
            f'netbox.netbox.netbox_{model}': {
                'netbox_url': '{{ netbox_url }}',
                'netbox_token': '{{ netbox_token }}',
                'state': 'absent',
                'data': '{{ item.data }}'
            },
            'loop': [item for item in copy.deepcopy(items_by_model[model]) if item.get('state') == 'absent'],
            'ignore_errors': True,
            'tags': [model, models[model].get('object_type')]
        })

    # Generate final playbook
    playbook = [{
        'name': 'Manage NetBox fixtures',
        'hosts': 'localhost',
        'connection': 'local',
        'collections':['netbox.netbox'],
        'gather_facts': False,
        'vars': {
            'netbox_url': "{{ lookup('ansible.builtin.env', 'NETBOX_URL') }}",
            'netbox_token': "{{ lookup('ansible.builtin.env', 'NETBOX_TOKEN') }}",
        },
        'tasks': tasks
    }]

    # Output the result as YAML
    print('# Autogenerated, do not edit')
    print(yaml.dump(playbook, default_flow_style=False, sort_keys=False))

if __name__ == '__main__':
    main()
