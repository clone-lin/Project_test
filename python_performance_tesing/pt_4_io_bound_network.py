# coding: utf-8
import asyncio
import multiprocessing
from concurrent import futures

import matplotlib.pyplot as plt

from misc import *
from threadpool import threadpool

Round = 10
CORE = 4
url_list = ['https://github.com/clone-lin/Project_test'] * 10

t_single_list = []
t_thread_list = []
t_process_list = []
t_futures_process_list = []
t_futures_thread_list = []
t_asyncio_list = []
t_asyncio_aiohttp_list = []


async def async_http_request(url):
    return http_requests(url)


"""
Single
"""
print('Try Single ...')

d = current_time()

for i in range(Round):
    s = current_time()
    [http_requests(url) for url in url_list]
    t_single_list.append(spend_time(s))

d_single = spend_time(d)

"""
Thread Pool
"""
print('Try Multi-Thread ...')

d = current_time()

for i in range(Round):
    s_time = current_time()

    thread_pool = threadpool(threads_count=CORE)
    thread_pool.start()
    for url in url_list:
        thread_pool.add(target=http_requests, args=(url,))
    thread_pool.wait()

    t_thread_list.append(spend_time(s_time))

d_thread = spend_time(d)

"""
Process Pool
"""

print('Try Multi-process ...')

d = current_time()

for i in range(Round):
    s_time = current_time()

    pool = multiprocessing.Pool(processes=CORE)
    for url in url_list:
        pool.apply_async(http_requests, args=(url,))
    pool.close()
    pool.join()

    t_process_list.append(spend_time(s_time))

d_process = spend_time(d)

"""
concurrent.futures Thread Pool
"""

print('Try concurrent.futures.ThreadPoolExecutor ...')

d = current_time()

for i in range(Round):
    s_time = current_time()

    with futures.ThreadPoolExecutor(max_workers=CORE) as executor:
        future_list = [executor.submit(http_requests, url) for url in url_list]
        for future in futures.as_completed(future_list):
            continue

    t_futures_thread_list.append(spend_time(s_time))

d_future_thread = spend_time(d)

"""
concurrent.futures Process Pool
"""

print('Try concurrent.futures.ProcessPoolExecutor ...')

d = current_time()

for i in range(Round):
    s_time = current_time()

    with futures.ProcessPoolExecutor(max_workers=CORE) as executor:
        future_list = [executor.submit(http_requests, url) for url in url_list]
        for future in futures.as_completed(future_list):
            continue

    t_futures_process_list.append(spend_time(s_time))

d_future_process = spend_time(d)

"""
Asyncio
"""

print('Try asyncio ...')

d = current_time()

loop = asyncio.get_event_loop()
for i in range(Round):
    future_list = []
    s_time = current_time()

    for url in url_list:
        future_list.append(asyncio.ensure_future(async_http_request(url)))
        # future_list.append(loop.run_in_executor(None, http_requests, url))
    loop.run_until_complete(asyncio.wait(future_list))

    t_asyncio_list.append(spend_time(s_time))

d_asyncio = spend_time(d)

"""
Asyncio + aiohttp
"""

print('Try asyncio + aiohttp ...')

d = current_time()

loop = asyncio.get_event_loop()
for i in range(Round):
    future_list = []
    s_time = current_time()

    for url in url_list:
        future_list.append(asyncio.ensure_future(async_http(url)))
    loop.run_until_complete(asyncio.wait(future_list))

    t_asyncio_aiohttp_list.append(spend_time(s_time))

d_asyncio_aiohttp = spend_time(d)

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
plt.plot(x, t_asyncio_aiohttp_list, label='Asyncio + Aiohttp (Total: %s)' % d_asyncio_aiohttp)
plt.title('Network IO Bound (R=%d, C=%d)' % (Round, CORE))
plt.xlabel('Test number')
plt.ylabel('Spend time(s)')
plt.legend()
plt.show()
