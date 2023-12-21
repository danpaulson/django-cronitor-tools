def cronitor_config(name: str = None, key: str = None, schedule: str = None,
                    schedule_tolerance: int = None, group: str = None, notify: str = None):
    def decorator(func):
        func._cronitor_config = {}
        if name is not None:
            func._cronitor_config['name'] = name
        if key is not None:
            func._cronitor_config['key'] = key
        if schedule is not None:
            func._cronitor_config['schedule'] = schedule
        if schedule_tolerance is not None:
            func._cronitor_config['schedule_tolerance'] = schedule_tolerance
        if group is not None:
            func._cronitor_config['group'] = group
        if notify is not None:
            func._cronitor_config['notify'] = notify
        return func
    return decorator
