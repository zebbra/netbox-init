FIELD_CHOICES = {
    'dcim.Device.status': (
        # - [offline, Offline, gray]
        ('planned', 'Planned', 'cyan'),
        ('installing', 'Installing', 'orange'),
        ('staged', 'Staged', 'blue'),
        ('active', 'Active', 'green'),
        ('maintenance', 'Maintenance', 'purple'),
        ('failed', 'Failed', 'red'),
        ('decommissioning', 'Decommissioning', 'yellow'),
    ),

    'dcim.Site.status': (
        ('planned', 'Planned', 'cyan'),
        ('staging', 'Staging', 'blue'),
        ('active', 'Active', 'green'),
        ('maintenance', 'Maintenance', 'purple'),
        ('decommissioning', 'Decommissioning', 'yellow'),
        ('retired', 'Retired', 'red'),
    )
}

PLUGINS = [
    'netbox_healthcheck_plugin',
]
