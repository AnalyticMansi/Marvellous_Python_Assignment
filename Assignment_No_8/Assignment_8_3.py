import threading

def evenlist(no):
    sum=0
    for i in no:
        if i % 2 == 0 :
            sum=sum+i
    print("Sum Of Even Numbers :- ",sum)

def oddlist(no):
    sum=0
    for i in no:
        if i % 2 != 0:
            sum=sum+i
    print("Sum of Odd Numbers :- ",sum)


def main():


    number = [1,2,3,4,5,6,7,8,9,10]

    T1=threading.Thread(target = evenlist,args=(number,))
    T2=threading.Thread(target = oddlist , args=(number,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()







if __name__ == "__main__":
    main()