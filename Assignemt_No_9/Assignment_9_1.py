import threading
import time

def thread_function(no):
    for i in range(6):
        print(i, end=" ")
        time.sleep(1)

def main():

    start_time = time.time()

    T1= threading.Thread(target = thread_function,args=(10000,))
    T2= threading.Thread(target = thread_function,args=(10000,))
    T3 = threading.Thread(target = thread_function,args=(10000,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    end_time = time.time()

    print("Time Requrie for execution is :-",end_time - start_time)


    print("End of main-----")



if __name__ =="__main__":
    main()