models = {
    "aggregate": {
        "dependencies": {"custom_field", "rir", "tags", "tenant"},
        "identifiers": ["prefix", "tenant"],
        "self_reference": [],
        "object_type": "aggregates"
    },
    "asn": {
        "dependencies": {"custom_field", "rir", "tags", "tenant"},
        "identifiers": ["asn", "tenant"],
        "self_reference": [],
        "object_type": "asns"
    },
    "cable": {
        "dependencies": {"custom_field", "tags", "tenant"},
        "identifiers": ["termination_a", "termination_b", "tenant"],
        "self_reference": [],
        "object_type": "cables"
    },
    "circuit": {
        "dependencies": {"circuit_type", "custom_field", "provider", "tags", "tenant"},
        "identifiers": ["cid", "tenant"],
        "self_reference": [],
        "object_type": "circuits"
    },
    "circuit_termination": {
        "dependencies": {"circuit", "custom_field", "site", "tags"},
        "identifiers": ["circuit", "term_side"],
        "self_reference": [],
        "object_type": "circuit-terminations"
    },
    "circuit_type": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "circuit-types"
    },
    "cluster": {
        "dependencies": {"cluster_group", "cluster_type", "custom_field", "site", "tags", "tenant"},
        "identifiers": ["name", "tenant"],
        "self_reference": [],
        "object_type": "clusters"
    },
    "cluster_group": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "cluster-groups"
    },
    "cluster_type": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "cluster-types"
    },
    "config_context": {
        "dependencies": {"cluster", "cluster_group", "cluster_type", "custom_field", "device_role", "device_type", "platform", "region", "site", "site_group", "tags", "tenant", "tenant_group"},
        "identifiers": ["name", "tenant"],
        "self_reference": [],
        "object_type": "config-contexts"
    },
    "config_template": {
        "dependencies": {"tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "config-templates"
    },
    "console_port": {
        "dependencies": {"cable", "custom_field", "device", "module", "tags"},
        "identifiers": ["device", "name"],
        "self_reference": [],
        "object_type": "console-ports"
    },
    "console_port_template": {
        "dependencies": {"device_type"},
        "identifiers": ["device_type", "name"],
        "self_reference": [],
        "object_type": "console-port-templates"
    },
    "console_server_port": {
        "dependencies": {"cable", "custom_field", "device", "tags"},
        "identifiers": ["device", "name"],
        "self_reference": [],
        "object_type": "console-server-ports"
    },
    "console_server_port_template": {
        "dependencies": {"device_type"},
        "identifiers": ["device_type", "name"],
        "self_reference": [],
        "object_type": "console-server-port-templates"
    },
    "contact": {
        "dependencies": {"contact_group", "custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "contacts"
    },
    "contact_group": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": ["parent_contact_group"],
        "object_type": "contact-groups"
    },
    "contact_role": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "contact-roles"
    },
    "custom_field": {
        "dependencies": {"custom_field_choice_set"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "custom-fields"
    },
    "custom_field_choice_set": {
        "dependencies": set(),
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "custom-field-choice-sets"
    },
    "custom_link": {
        "dependencies": set(),
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "custom-links"
    },
    "device": {
        "dependencies": {"cluster", "config_template", "custom_field", "device_role", "device_type", "location", "platform", "rack", "site", "tags", "tenant", "virtual_chassis"},
        "identifiers": ["name", "tenant"],
        "self_reference": [],
        "object_type": "devices"
    },
    "device_bay": {
        "dependencies": {"device", "tags"},
        "identifiers": ["device", "name"],
        "self_reference": [],
        "object_type": "device-bays"
    },
    "device_bay_template": {
        "dependencies": {"device_type"},
        "identifiers": ["device_type", "name"],
        "self_reference": [],
        "object_type": "device-bay-templates"
    },
    "device_interface": {
        "dependencies": {"custom_field", "device", "tags", "vlan"},
        "identifiers": ["device", "name"],
        "self_reference": ["parent_interface"],
        "object_type": "interfaces"
    },
    "device_interface_template": {
        "dependencies": {"device_type"},
        "identifiers": ["device_type", "name"],
        "self_reference": [],
        "object_type": "interface-templates"
    },
    "device_role": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "device-roles"
    },
    "device_type": {
        "dependencies": {"custom_field", "manufacturer", "platform", "tags"},
        "identifiers": ["model"],
        "self_reference": [],
        "object_type": "device-types"
    },
    "export_template": {
        "dependencies": set(),
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "export-templates"
    },
    "fhrp_group": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["group_id"],
        "self_reference": [],
        "object_type": "fhrp-groups"
    },
    "fhrp_group_assignment": {
        "dependencies": set(),
        "identifiers": ["fhrp_group", "interface_id"],
        "self_reference": [],
        "object_type": "fhrp-group-assignments"
    },
    "front_port": {
        "dependencies": {"custom_field", "device", "tags"},
        "identifiers": ["device", "name"],
        "self_reference": [],
        "object_type": "front-ports"
    },
    "front_port_template": {
        "dependencies": {"device_type", "rear_port_template"},
        "identifiers": ["device_type", "name"],
        "self_reference": [],
        "object_type": "front-port-templates"
    },
    "inventory_item": {
        "dependencies": {"custom_field", "device", "manufacturer", "inventory_item_role", "tags"},
        "identifiers": ["name"],
        "self_reference": ["parent_inventory_item"],
        "object_type": "inventory-items"
    },
    "inventory_item_role": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "inventory-item-roles"
    },
    "ip_address": {
        "dependencies": {"custom_field", "device", "device_interface", "prefix", "tags", "tenant", "virtual_machine", "vrf"},
        "identifiers": ["address", "tenant"],
        "self_reference": [],
        "object_type": "ip-addresses"
    },
    "ipam_role": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "roles"
    },
    "journal_entry": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": [],
        "self_reference": [],
        "object_type": "journal-entries"
    },
    "l2vpn": {
        "dependencies": {"custom_field", "tags", "tenant"},
        "identifiers": ["name", "tenant"],
        "self_reference": [],
        "object_type": "l2vpns"
    },
    "l2vpn_termination": {
        "dependencies": {"custom_field", "device_interface", "l2vpn", "tags", "vlan", "vm_interface"},
        "identifiers": ["assigned_object_id", "assigned_object_typee", "l2vpn"],
        "self_reference": [],
        "object_type": "l2vpn-terminations"
    },
    "location": {
        "dependencies": {"custom_field", "site", "tags", "tenant"},
        "identifiers": ["name", "tenant"],
        "self_reference": ["parent_location"],
        "object_type": "locations"
    },
    "manufacturer": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "manufacturers"
    },
    "module": {
        "dependencies": {"custom_field", "device", "module_bay", "module_type", "tags"},
        "identifiers": ["device", "module_bay"],
        "self_reference": [],
        "object_type": "modules"
    },
    "module_bay": {
        "dependencies": {"custom_field", "device", "tags"},
        "identifiers": ["device", "name"],
        "self_reference": [],
        "object_type": "module-bays"
    },
    "module_type": {
        "dependencies": {"custom_field", "manufacturer", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "module-types"
    },
    "permission": {
        "dependencies": set(),
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "permissions"
    },
    "platform": {
        "dependencies": {"custom_field", "config_template", "manufacturer", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "platforms"
    },
    "netbox_power_feed": {
        "dependencies": {"custom_field", "power_panel", "rack", "tags"},
        "identifiers": ["name", "power_panel"],
        "self_reference": [],
        "object_type": "power-feeds"
    },
    "netbox_power_outlet": {
        "dependencies": {"device", "power_port", "tags"},
        "identifiers": ["device_name"],
        "self_reference": [],
        "object_type": "power-outlets"
    },
    "power_outlet_template": {
        "dependencies": {"device_type", "power_port_template"},
        "identifiers": ["device_type", "name"],
        "self_reference": [],
        "object_type": "power-outlet-templates"
    },
    "power_panel": {
        "dependencies": {"custom_field", "location", "rack_group", "site", "tags"},
        "identifiers": ["name", "site"],
        "self_reference": [],
        "object_type": "power-panels"
    },
    "power_port": {
        "dependencies": {"custom_field", "device", "tags"},
        "identifiers": ["device", "name"],
        "self_reference": [],
        "object_type": "power-ports"
    },
    "power_port_template": {
        "dependencies": {"device_type", "module_type"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "power-port-templates"
    },
    "prefix": {
        "dependencies": {"custom_field", "site", "tags", "tenant", "vlan", "vrf"},
        "identifiers": ["prefix", "tenant"],
        "self_reference": ["parent"],
        "object_type": "prefixes"
    },
    "provider": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "providers"
    },
    "provider_network": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name", "provider"],
        "self_reference": [],
        "object_type": "provider-networks"
    },
    "rack": {
        "dependencies": {"custom_field", "location", "rack_group", "rack_role", "site", "tags", "tenant"},
        "identifiers": ["name", "tenant"],
        "self_reference": [],
        "object_type": "racks"
    },
    "rack_group": {
        "dependencies": {"site"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "rack-groups"
    },
    "rack_role": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "rack-roles"
    },
    "rear_port": {
        "dependencies": {"device", "tags"},
        "identifiers": ["device", "name"],
        "self_reference": [],
        "object_type": "rear-ports"
    },
    "rear_port_template": {
        "dependencies": {"device_type"},
        "identifiers": ["device_type", "name"],
        "self_reference": [],
        "object_type": "rear-port-templates"
    },
    "region": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": ["parent_region"],
        "object_type": "regions"
    },
    "rir": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "rirs"
    },
    "route_target": {
        "dependencies": {"custom_field", "tags", "tenant"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "route-targets"
    },
    "service": {
        "dependencies": {"custom_field", "device", "ip_address", "tags", "virtual_machine"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "services"
    },
    "service_template": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "service-templates"
    },
    "site": {
        "dependencies": {"custom_field", "region", "site_group", "tags", "tenant"},
        "identifiers": ["name", "tenant"],
        "self_reference": [],
        "object_type": "sites"
    },
    "site_group": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": ["parent_site_group"],
        "object_type": "site-groups"
    },
    "tag": {
        "dependencies": set(),
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "tags"
    },
    "tenant": {
        "dependencies": {"custom_field", "tags", "tenant_group"},
        "identifiers": ["tenant"],
        "self_reference": [],
        "object_type": "tenants"
    },
    "tenant_group": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": ["parent_tenant_group"],
        "object_type": "tenant-groups"
    },
    "token": {
        "dependencies": {"user"},
        "identifiers": ["key"],
        "self_reference": [],
        "object_type": "tokens"
    },
    "tunnel": {
        "dependencies": {"custom_field", "tags", "tenant", "tunnel_group"},
        "identifiers": ["name", "tenant"],
        "self_reference": [],
        "object_type": "tunnels"
    },
    "tunnel_group": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "tunnel-groups"
    },
    "user": {
        "dependencies": {"permission", "user_group"},
        "identifiers": ["username"],
        "self_reference": [],
        "object_type": "users"
    },
    "user_group": {
        "dependencies": {"permission"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "user-groups"
    },
    "virtual_chassis": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "virtual-chassis"
    },
    "virtual_disk": {
        "dependencies": {"custom_field", "tags", "virtual_machine"},
        "identifiers": ["name", "virtual_machine"],
        "self_reference": [],
        "object_type": "virtual-disks"
    },
    "virtual_machine": {
        "dependencies": {"cluster", "config_template", "custom_field", "device", "device_role", "platform", "site", "tags", "tenant"},
        "identifiers": ["name", "tenant"],
        "self_reference": [],
        "object_type": "virtual-machines"
    },
    "vlan": {
        "dependencies": {"custom_field", "site", "tags", "tenant", "vlan_group"},
        "identifiers": ["name", "tenant"],
        "self_reference": [],
        "object_type": "vlans"
    },
    "vlan_group": {
        "dependencies": {"custom_field", "site", "tags"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "vlan-groups"
    },
    "vm_interface": {
        "dependencies": {"custom_field", "tags", "tenant", "vlan", "virtual_machine", "vrf"},
        "identifiers": ["name", "virtual_machine"],
        "self_reference": ["parent_vm_interface"],
        "object_type": "interfaces"
    },
    "vrf": {
        "dependencies": {"custom_field", "tags", "tenant"},
        "identifiers": ["name", "tenant"],
        "self_reference": [],
        "object_type": "vrfs"
    },
    "webhook": {
        "dependencies": {"custom_field", "tags", "tenant"},
        "identifiers": ["name"],
        "self_reference": [],
        "object_type": "webhooks"
    },
    "wireless_lan": {
        "dependencies": {"custom_field", "tags", "wireless_lan_group", "vlan"},
        "identifiers": ["ssid"],
        "self_reference": [],
        "object_type": "wireless-lans"
    },
    "wireless_lan_group": {
        "dependencies": {"custom_field", "tags"},
        "identifiers": ["name"],
        "self_reference": ["parent_wireless_lan_group"],
        "object_type": "wireless-lan-groups"
    },
    "wireless_link": {
        "dependencies": {"custom_field", "device_interface", "tags"},
        "identifiers": ["interface_a", "interface_b"],
        "self_reference": [],
        "object_type": "wireless-links"
    }
}
