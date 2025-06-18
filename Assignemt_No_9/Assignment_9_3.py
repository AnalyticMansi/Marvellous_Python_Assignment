import os
import time
import multiprocessing

def factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact=fact*i
    return fact

def main():

    start_time = time.time()

    data = [3,5,7,10,12]
    result = []

    p = multiprocessing.Pool()
    result = p.map(factorial,data)
    
    p.close()
    p.join()

    print(result)
    end_time = time.time()
    print("Time Requrie for execution is :-",end_time - start_time)
    


if __name__ == "__main__":
    main()