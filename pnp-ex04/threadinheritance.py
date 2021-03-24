import threading

class MyThread(threading.Thread):
    def run(self):
        
        print("Thread is running")

mt = MyThread()
mt.start()



