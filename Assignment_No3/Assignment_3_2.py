
def Maximum(No):
    result=max(No)
    return result

def main():

    print("Enter Number of elements :- ")
    size=int(input())

    Data=list()

    print("Enter Elememts:-")
    for i in range (size):
        no=int(input())
        Data.append(no)

    print("Input Elements are :- ")
    for value in Data:
        print(value)

    ans = Maximum(Data)
    print("Maximum Number is :-",ans)

    


if __name__ == "__main__":
    main()