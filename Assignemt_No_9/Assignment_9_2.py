import threading
import time
import multiprocessing

def square(no):
    num = no * no
    print(num)

def main():

    numbers=[1,2,3,4,5]
    start_time = time.time()

    for no in numbers:

        p1=multiprocessing.Process(target = square ,args=(no,))
        
        p1.start()
        p1.join()

    end_time = time.time()

    print("Time Requrie for execution is :-",end_time - start_time)


    print("End of main-----")



if __name__ =="__main__":
    main()