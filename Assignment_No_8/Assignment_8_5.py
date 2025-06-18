import threading
import time

def thread1():
    for i in range(1,51):
        print(i,end=" ")
    print("-----------------------","\n")
    time.sleep(0.01)

def thread2():
    for i in range(50,0,-1):
        print(i,end= " ") 

def main():

    T1=threading.Thread(target = thread1)
    T2=threading.Thread(target= thread2)

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ =="__main__":
    main()

