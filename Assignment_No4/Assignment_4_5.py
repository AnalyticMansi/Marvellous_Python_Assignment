from functools import reduce

def prime(No):
    if No <= 1:
        return False
    if No == 2:
        return True
    if No % 2 == 0:
        return False
    for i in range(3, No // 2 + 1, 2):
        if No % i == 0:
            return False
    return True
           

def Multi(No):
    return (No*2)

def Maximum(A,B):
    return max(A,B)


def main():

    print("Enter no of elements :- ")
    size=int(input())

    Data=list()

    print("Enter the elements :-")
    print("---------------------")
    for i in range(size):
        no=int(input())
        Data.append(no)

    print("Input elemetns are :-",Data)

    FData = list(filter(prime,Data))
    print("Filter Data :-",FData)

    MData = list(map(Multi,FData))
    print("Map Data :-",MData)

    RData = reduce(Maximum,MData)
    print("Reduce Data :-",RData)




if __name__ == "__main__":
    main()