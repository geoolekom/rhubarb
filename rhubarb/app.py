from jsonschema import validate

from rhubarb.storage import DefaultTaskQueue

registered_tasks = {}


class AbstractApp(object):
    task_queue = None

    def queue_task(self, task_name, params):
        task = registered_tasks.get(task_name)
        if task:
            validate(params, task.json_schema)
            self.task_queue.put(task_name, params)

    def perform_task(self):
        task_name, params = self.task_queue.get()
        task = registered_tasks.get(task_name)
        if task:
            print(f'{task_name}:\tпринято в обработку.')
            result = task(**params)
            return result
        else:
            print(f'{task_name}:\tзадача не существует.')

    def handle_result(self, result):
        raise NotImplementedError('Необходимо реализовать метод для обработки результата задачи.')

    def run(self):
        print('Зарегистрированные задачи:')
        for name in registered_tasks:
            print(f'- {name}')
        try:
            while True:
                result = self.perform_task()
                self.handle_result(result)
        except KeyboardInterrupt:
            print('Выполнение прервано пользователем.')


class DefaultApp(AbstractApp):
    task_queue = DefaultTaskQueue()

    def handle_result(self, result):
        print(result)
