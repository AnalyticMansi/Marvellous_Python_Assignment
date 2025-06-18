import threading


def evenfactor(no):
    sum=0
    for i in range(1,no+1):
        if no % 1 == 0 and i % 2 == 0:
            sum = sum+i
    print("Sum of Even Factors:- ",sum)


def oddfactor(no):
    sum=0
    for i in range(1,no+1):
        if no % 1 == 0 and i % 2 !=0:
            sum=sum+i
    print("Sum of Odd Factors :-",sum)



def main():


    number = int(input("Enetr A Number :- "))


    T1=threading.Thread(target=oddfactor , args=(number,))
    T2=threading.Thread(target =evenfactor  , args=(number,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit in main")


if __name__ == "__main__":
    main()