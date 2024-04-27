'''
File: shared-memory-process.py
Author: Chuncheng Zhang
Purpose:
    The script provides an example of how to use a shared memory across process
'''
# %%
import time

from threading import Thread
from multiprocessing import Process
from multiprocessing.managers import SharedMemoryManager

# %%


class MyObject(object):
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def print(self, prefix='>> '):
        print('%s, num1: %d, num2: %d' % (prefix, self.num1, self.num2))


# %%


def function1(mem, obj):
    while True:
        for j in range(5, 10):
            mem[j] += 2
        obj.num1 += 2
        obj.print('F1')
        print('F1', mem)
        time.sleep(0.1)


def function2(mem, obj):
    while True:
        for j in range(0, 5):
            mem[j] += 1
        obj.num2 += 1
        obj.print('F2')
        print('F2', mem)
        time.sleep(0.1)


# %%
if __name__ == '__main__':
    obj = MyObject()

    method = Thread
    method = Process

    with SharedMemoryManager() as smm:
        sl = smm.ShareableList([0 for _ in range(10)])

        p1 = method(target=function1, args=(sl, obj,), daemon=True)
        p2 = method(target=function2, args=(sl, obj,), daemon=True)

        p1.start()
        p2.start()

        for j in range(10):
            obj.print('M')
            print('M', j, sl)
            time.sleep(0.1)

    print('Done.')
