from multiprocessing import Queue


class AbstractTaskQueue(object):
    def get(self):
        raise NotImplementedError('Реализуйте метод get')

    def put(self, task_name, params):
        raise NotImplementedError('Реализуйте метод put')


class DefaultTaskQueue(AbstractTaskQueue):
    def __init__(self):
        self._q = Queue()

    def get(self):
        return self._q.get()

    def put(self, task_name, params):
        self._q.put((task_name, params))
