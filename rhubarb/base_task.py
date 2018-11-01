from jsonschema import validate

from rhubarb.storage import tasks


class BaseTaskMetaclass(type):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        if instance.name:
            tasks[instance.name] = instance()
        return instance


class BaseTask(metaclass=BaseTaskMetaclass):
    name = None
    json_schema = None

    def run(self, *args, **kwargs):
        raise NotImplementedError('Необходимо переопределить метод run в дочернем классе.')

    def __call__(self, **kwargs):
        if self.json_schema:
            validate(kwargs, self.json_schema)
        return self.run(**kwargs)
