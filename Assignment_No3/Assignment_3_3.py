def Minimum(No):
    result= min(No)
    return result

def main():

    print("Enter Number of elements :- ")
    size = int(input())

    Data=list()

    print("Enter elements :- ")
    for i in range(size):
        no=int(input())
        Data.append(no)

    print("Input elements are :- ")
    for value in Data:
        print(value)

    
    ans=Minimum(Data)
    print("Minimun Number is  :- ",ans)


if __name__ =="__main__":
    main()