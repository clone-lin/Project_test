# coding: utf-8
import matplotlib.pyplot as plt

from misc import *

Round = 10
url_list = ['https://github.com/clone-lin/Project_test'] * 2

t_cpu_list = []
t_io_list = []
t_urllib_list = []
t_requests_list = []

for i in range(Round):
    print('Round %d ...' % (i + 1))

    # CPU Bound
    s = current_time()
    count(1, 1)
    t_cpu_list.append(spend_time(s))

    # IO Bound
    s = current_time()
    write_file()
    read_file()
    t_io_list.append(spend_time(s))

    # Network request
    s = current_time()
    [http_urllib(url) for url in url_list]
    t_urllib_list.append(spend_time(s))

    s = current_time()
    [http_requests(url) for url in url_list]
    t_requests_list.append(spend_time(s))

# Draw
x = list(range(1, Round + 1))
plt.plot(x, t_cpu_list, label='CPU Bound')
plt.plot(x, t_io_list, label='IO Bound')
plt.plot(x, t_urllib_list, label='urllib')
plt.plot(x, t_requests_list, label='requests')
plt.title('Performance Testing (R=%d)' % Round)
plt.xlabel('Test number')
plt.ylabel('Spend time(s)')
plt.legend()
plt.show()
