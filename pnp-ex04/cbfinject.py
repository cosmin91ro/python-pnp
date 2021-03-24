import threading,time

def cbf():
    id = threading.get_ident() 
    print(f"Hello from thread {id}")

t = threading.Thread(None,cbf)

for i in range(10):
    t = threading.Thread(None,cbf)
    t.start()




