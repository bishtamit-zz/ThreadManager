import time

from threadmanager import ThreadManager


def infinite(id_):
    while 1:
        print('running with id', id_)
        time.sleep(1)


obj = ThreadManager.run_parallel(n_iter=3, funclist=[infinite])
while 1:
    time.sleep(10)
    pass
