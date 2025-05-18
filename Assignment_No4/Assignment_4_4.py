from functools import reduce

def Even(No):
    return (No%2==0)

def sum(No):
    return (No*No)

def product(A,B):
    return (A+B)


def main():

    print("Enter no of elements  :- ")
    size=int(input())

    Data=list()
   
    print("Enter Elements :-")
    print("-------------------")
    for i in range(size):
        no=int(input())
        Data.append(no)
    print("Input Elements are",Data)
    print("--------------------------")


    FData = list(filter(Even,Data))
    print("Filter Output :- ",FData)

    MData = list(map(sum,FData))
    print("Map Output :- ",MData)

    RData = reduce(product,MData)
    print("Reduce output :-",RData)


if __name__ =="__main__":
    main()