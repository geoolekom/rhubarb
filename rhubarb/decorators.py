from jsonschema import validate

from rhubarb.app import registered_tasks


def task(name, json_schema=None):
    def decorator(func):
        def inner(**kwargs):
            if json_schema:
                validate(kwargs, json_schema)
            return func(**kwargs)
        inner.json_schema = json_schema
        registered_tasks[name] = inner
        return inner
    return decorator
