import multiprocessing
import threading
import time

def simple_sum():
    total=0
    for i in range(1,10000001):
        total = total+i
    print("Sum is :-",total)



def main():

    print("Comparing Exwcution Time")

    start_time = time.time()
    simple_sum()
    end_time = time.time()
    print("Normale Time:-",end_time - start_time,"\n")

    
    start_time = time.time()
    T1=threading.Thread(target =simple_sum)
    T1.start()
    T1.join()
    end_time = time.time()
    print("Threading Time :-",end_time - start_time ,"\n")


    start_time = time.time()
    p1=multiprocessing.Process(target=simple_sum)
    p1.start()
    p1.join()
    end_time = time.time()
    print("Multiprocessing Time :-",end_time - start_time,"\n")



if __name__ =="__main__":
    main()