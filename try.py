import threading

def worker(a):
    print(a*2)
a=2
th1=threading.Thread(target=worker,args=(a,))
th1.start()