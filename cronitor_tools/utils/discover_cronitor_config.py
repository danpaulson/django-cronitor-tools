import importlib
import pkgutil


def discover_cronitor_tasks(package_name):
    package = importlib.import_module(package_name)
    cronitor_tasks = []
    for _, module_name, _ in pkgutil.walk_packages(package.__path__, package_name + '.'):
        module = importlib.import_module(module_name)
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if callable(attr) and hasattr(attr, '_cronitor_config'):
                cronitor_tasks.append(getattr(attr, '_cronitor_config'))
    return cronitor_tasks
