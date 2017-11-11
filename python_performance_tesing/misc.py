# coding: utf-8
import time
import urllib.request

import aiofiles
import aiohttp
import requests

__all__ = ['current_time', 'spend_time',
           'count',
           'write_file', 'read_file', 'async_write_file', 'async_read_file',
           'http_urllib', 'http_requests', 'async_http']


def current_time():
    return time.time()


def spend_time(stime):
    duration = time.time() - stime
    return round(duration, 3)


"""
CPU Bound
"""


def count(x, y):
    c = 0
    while c < 100000:
        c += 1
        x += x
        y += y


"""
IO Bound
"""


def write_file(filename='test.txt'):
    f = open(filename, "w")
    for x in range(1000000):
        f.write("testwrite\n")
    f.close()


def read_file(filename='test.txt'):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()


async def async_write_file(filename='test.txt'):
    async with aiofiles.open(filename, "w") as f:
        for x in range(1000000):
            await f.write("testwrite\n")


async def async_read_file(filename='test.txt'):
    async with aiofiles.open(filename, "r") as f:
        lines = await f.readlines()


"""
Network request
"""


def http_urllib(url):
    req = urllib.request.Request(url, headers={'user-agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req)

    charset = res.info().get_content_charset()
    data = res.read().decode(charset)

    return res.status, data


def http_requests(url):
    res = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})
    return res.status_code, res.text


async def async_http(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            return res.status, await res.text(errors='ignore')
