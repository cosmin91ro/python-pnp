import threading, time

class MyThread(threading.Thread):
    active = False
    def stop_thread(self):
        self.active = False
    def run(self): 
            self.active = True
            print("I am going to sleep 10 seconds")
            for i in range(10000):
                time.sleep(0.001)
                if not self.active:
                    return
                print("Thread is running")

mt = MyThread() 
mt.start()  
time.sleep(2)
print("Hey, wake up!")
mt.stop_thread()

