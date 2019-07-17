import threading

class ThreadManager:

    @classmethod
    def run_parallel(cls, n_iter=None, funclist=[], stoppable=False):
        thr = threading.Thread(target=cls,
                         args=(n_iter, funclist, stoppable),
                         name='TM_parallel', daemon=True
                         )
        thr.start()
        return thr

    def __init__(self, n_iter=None, funclist=[], stoppable=False):
        self.started_threads = []
        self.running_threads = []

        self.n_iter = n_iter
        self.funclist = funclist

        if n_iter and funclist:
            self.run([funclist[0] for _ in range(n_iter)])
        elif n_iter and not funclist:
            raise Exception('Pass atleast one targetname in funclist')
        elif not n_iter and funclist:
            self.run(funclist)
        else:
            raise Exception('Pass n_iter or funclist, both cannot be empty')

    def run(self, run_on):
        
        print(run_on)

    def restart_stopped(self):
        pass

    def stop_running(self):
        pass