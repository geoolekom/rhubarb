from rhubarb.storage import DefaultTaskQueue

registered_tasks = {}


class AbstractApp(object):
    task_queue = None

    def perform_task(self):

        task_name, params = self.task_queue.get()
        task = registered_tasks.get(task_name)
        if task:
            result = task(**params)
            return result

    def handle_result(self, result):
        raise NotImplementedError('Необходимо реализовать метод для обработки результата задачи.')

    def run(self):
        try:
            while True:
                result = self.perform_task()
                self.handle_result(result)
        except KeyboardInterrupt:
            print('Выполнение прервано пользователем.')
        except Exception as e:
            print(f'Произошла ошибка: {e}')


class DefaultApp(AbstractApp):
    task_queue = DefaultTaskQueue()

    def handle_result(self, result):
        print(result)
