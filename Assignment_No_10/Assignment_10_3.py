from functools import reduce


def greater(no):
    return (no>=70 and no<=90) 

def increase(no):
    return (no + 10)

def product(A,B):
    return(A*B)

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

    FData = list(filter(greater,Data))
    print("Filter Output",FData)
    print("------------------------------")

    MData = list(map(increase,FData))
    print("Map Output",MData)
    print("------------------------------")

    RData = reduce(product,MData)
    print("Reduce Output",RData)


if __name__ =="__main__":
    main()