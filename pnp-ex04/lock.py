import threading
import time

locker = threading.Lock()

class MyThread(threading.Thread):
    def run(self):
        locker.acquire()
        for i in range(10):
            print(i)
            time.sleep(0.5)
        locker.release()

mt1 = MyThread()
mt2 = MyThread()
mt1.start()
mt2.start()
