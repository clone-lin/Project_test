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
t_futures_process_list = []
t_futures_thread_list = []
t_asyncio_list = []
t_asyncio_aiofiles_list = []


def do_io(i):
    s_time = current_time()
    filename = 'test_%d.txt' % (i + 1)
    write_file(filename)
    read_file(filename)
    return spend_time(s_time)


def thread_io(i, thread_queue):
    thread_queue.put(do_io(i))


def process_io(i, process_queue):
    process_queue.put(do_io(i))


async def asyncio_io(i):
    return do_io(i)


async def aiofiles_io(i):
    s_time = current_time()
    filename = 'test_%d.txt' % (i + 1)
    await async_write_file(filename)
    await async_read_file(filename)
    return spend_time(s_time)


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
    write_file()
    read_file()
    t_single_list.append(spend_time(s))

d_single = spend_time(d)

"""
Thread Pool
"""
print('Try Multi-Thread ...')

d = current_time()

thread_pool = threadpool(threads_count=CORE)
thread_pool.start()
q_thread = queue.Queue()
for i in range(Round):
    thread_pool.add(target=thread_io, args=(i, q_thread,))
thread_pool.wait()

t_thread_list = empty_queue(q_thread)

d_thread = spend_time(d)

"""
Process Pool
"""

print('Try Multi-process ...')

d = current_time()

pool = multiprocessing.Pool(processes=CORE)
m = multiprocessing.Manager()
q_process = m.Queue()
for i in range(Round):
    pool.apply_async(process_io, args=(i, q_process,))
pool.close()
pool.join()

t_process_list = empty_queue(q_process)

d_process = spend_time(d)

"""
Asyncio + concurrent.futures Thread Pool
"""

print('Try Asyncio + concurrent.futures.ThreadPoolExecutor ...')

d = current_time()

loop = asyncio.get_event_loop()
executor = futures.ThreadPoolExecutor(max_workers=CORE)

future_list = []
for i in range(Round):
    future_list.append(loop.run_in_executor(executor, do_io, i))

tasks_done, pending = loop.run_until_complete(asyncio.wait(future_list))
t_futures_thread_list = [task.result() for task in tasks_done]

d_asyncio_thread = spend_time(d)

"""
Asyncio + concurrent.futures Process Pool
"""

print('Try Asyncio + concurrent.futures.ProcessPoolExecutor ...')

d = current_time()

loop = asyncio.get_event_loop()
executor = futures.ProcessPoolExecutor(max_workers=CORE)
future_list = []
for i in range(Round):
    future_list.append(loop.run_in_executor(executor, do_io, i))

tasks_done, pending = loop.run_until_complete(asyncio.wait(future_list))
t_futures_process_list = [task.result() for task in tasks_done]

d_asyncio_process = spend_time(d)

"""
Asyncio
"""

print('Try asyncio ...')

d = current_time()

loop = asyncio.get_event_loop()
future_list = []
for i in range(Round):
    future_list.append(asyncio.ensure_future(asyncio_io(i)))
tasks_done, pending = loop.run_until_complete(asyncio.wait(future_list))
t_asyncio_list = [task.result() for task in tasks_done]

d_asyncio = spend_time(d)

"""
Asyncio + aiofiles
"""

print('Try asyncio + aiofiles ...')

d = current_time()

loop = asyncio.get_event_loop()
future_list = []
for i in range(Round):
    future_list.append(asyncio.ensure_future(aiofiles_io(i)))
tasks_done, pending = loop.run_until_complete(asyncio.wait(future_list))
t_asyncio_aiofiles_list = [task.result() for task in tasks_done]

d_asyncio_aiofiles = spend_time(d)

"""
Draw
"""

x = list(range(1, Round + 1))
plt.plot(x, t_single_list, label='Single (Total: %s)' % d_single)
plt.plot(x, t_thread_list, label='Multi-thread (Total: %s)' % d_thread)
plt.plot(x, t_process_list, label='Multi-process (Total: %s)' % d_process)
plt.plot(x, t_futures_thread_list, label='ThreadPoolExecutor (Total: %s)' % d_asyncio_thread)
plt.plot(x, t_futures_process_list, label='ProcessPoolExecutor (Total: %s)' % d_asyncio_process)
plt.plot(x, t_asyncio_list, label='Asyncio (Total: %s)' % d_asyncio)
plt.plot(x, t_asyncio_aiofiles_list, label='Asyncio + aiofiles (Total: %s)' % d_asyncio_aiofiles)
plt.title('File IO Bound (R=%d, C=%d)' % (Round, CORE))
plt.xlabel('Test number')
plt.ylabel('Spend time(s)')
plt.legend()
plt.show()
