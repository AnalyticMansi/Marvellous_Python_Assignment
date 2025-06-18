from functools import reduce


def CheckEven(No):
    return (No%2 == 0)

def square(no):
    return (no * no)

def Sum(A,B):
    return (A+B)


def main():

    Data =[]

    print("Enter Number of Elements :- ")
    size = int(input())


    print("Please Enter Numeric Values :- ")
    for i in range (size):
        No=int(input())
        Data.append(No)


    print("Input data :-",Data)
    print("--------------------------------")

    FData = list(filter(CheckEven,Data))
    print("Filter Output",FData)
    print("------------------------------")

    MData = list(map(square,FData))
    print("Map Output",MData)
    print("------------------------------")

    RData = reduce(Sum,MData)
    print("Reduce Output",RData)


if __name__ =="__main__":
    main()