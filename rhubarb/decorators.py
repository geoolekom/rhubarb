from jsonschema import validate

from rhubarb.storage import tasks


def task(name, json_schema=None):
    def decorator(func):
        def inner(**kwargs):
            if json_schema:
                validate(kwargs, json_schema)
            return func(**kwargs)
        tasks[name] = inner
        return inner
    return decorator
