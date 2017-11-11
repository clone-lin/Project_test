# coding: utf-8
from queue import Queue
from threading import Thread

# Stop event of thread
StopEvent = object()


class threadpool:
    def __init__(self, threads_count=10, queue=None):
        self._thread_count = threads_count
        self._queue = queue or Queue()
        self._threads = []

    def start(self):
        assert len(self._threads) == 0

        for i in range(self._thread_count):
            thread = Thread(target=_worker, kwargs={'queue': self._queue})
            thread.start()
            self._threads.append(thread)

    def add(self, target=None, args=(), kwargs={}):
        self._queue.put(tuple([target, args, kwargs]))

    def wait(self):
        for i in range(self._thread_count):
            self._queue.put(StopEvent)

        for i in self._threads:
            if i.isAlive():
                i.join()


def _worker(queue):
    while True:
        try:
            task = queue.get()
            if task is StopEvent:
                # Get a break request, finish work
                break

            target, args, kwargs = task
            if target:
                resp = target(*args, **kwargs)
            queue.task_done()
        except Exception as err:
            queue.task_done()
            continue
