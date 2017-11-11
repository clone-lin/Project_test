# coding: utf-8
import asyncio
import multiprocessing
import queue
from concurrent import futures

import matplotlib.pyplot as plt

from misc import *
from threadpool import threadpool

Round = 30
CORE = 4

t_single_list = []
t_thread_list = []
t_process_list = []
t_futures_thread_list = []
t_futures_process_list = []
t_asyncio_list = []


def do_count():
    s_time = current_time()
    count(1, 1)
    return spend_time(s_time)


async def async_do_count():
    return do_count()


def thread_count(thread_queue):
    thread_queue.put(do_count())


def process_count(process_queue):
    process_queue.put(do_count())


def empty_queue(q):
    ret_list = []
    while q.qsize() != 0:
        ret_list.append(q.get())
    return ret_list


"""
Single
"""
print('Try Single ...')

d = current_time()

for i in range(Round):
    s = current_time()
    count(1, 1)
    t_single_list.append(spend_time(s))

d_single = spend_time(d)

"""
Thread Pool
"""
print('Try Multi-Thread ...')

d = current_time()

thread_pool = threadpool(threads_count=CORE)
q_thread = queue.Queue()
for i in range(Round):
    thread_pool.add(target=thread_count, args=(q_thread,))
thread_pool.start()
thread_pool.wait()

t_thread_list = empty_queue(q_thread)

d_thread = spend_time(d)

"""
Process Pool
"""

print('Try Multi-process ...')

d = current_time()

process_pool = multiprocessing.Pool(processes=CORE)
m = multiprocessing.Manager()
q_process = m.Queue()
for i in range(Round):
    process_pool.apply_async(process_count, args=(q_process,))
process_pool.close()
process_pool.join()

t_process_list = empty_queue(q_process)

d_process = spend_time(d)

"""
concurrent.futures Thread Pool
"""

print('Try concurrent.futures.ThreadPoolExecutor ...')

d = current_time()

with futures.ThreadPoolExecutor(max_workers=CORE) as executor:
    future_list = [executor.submit(do_count) for i in range(Round)]
    for future in futures.as_completed(future_list):
        t_futures_thread_list.append(future.result())

d_future_thread = spend_time(d)

"""
concurrent.futures Process Pool
"""

print('Try concurrent.futures.ProcessPoolExecutor ...')

d = current_time()

with futures.ProcessPoolExecutor(max_workers=CORE) as executor:
    future_list = [executor.submit(do_count) for i in range(Round)]
    for future in futures.as_completed(future_list):
        t_futures_process_list.append(future.result())

d_future_process = spend_time(d)

"""
Asyncio
"""

print('Try asyncio ...')

d = current_time()

loop = asyncio.get_event_loop()
future_list = []
for i in range(Round):
    future_list.append(asyncio.ensure_future(async_do_count()))
tasks_done, pending = loop.run_until_complete(asyncio.wait(future_list))
t_asyncio_list = [task.result() for task in tasks_done]

d_asyncio = spend_time(d)

"""
Draw
"""

x = list(range(1, Round + 1))
plt.plot(x, t_single_list, label='Single (Total: %s)' % d_single)
plt.plot(x, t_thread_list, label='Multi-thread (Total: %s)' % d_thread)
plt.plot(x, t_process_list, label='Multi-process (Total: %s)' % d_process)
plt.plot(x, t_futures_thread_list, label='ThreadPoolExecutor (Total: %s)' % d_future_thread)
plt.plot(x, t_futures_process_list, label='ProcessPoolExecutor (Total: %s)' % d_future_process)
plt.plot(x, t_asyncio_list, label='Asyncio (Total: %s)' % d_asyncio)
plt.title('CPU Bound (R=%d, C=%d)' % (Round, CORE))
plt.xlabel('Test number')
plt.ylabel('Spend time(s)')
plt.legend()
plt.show()
