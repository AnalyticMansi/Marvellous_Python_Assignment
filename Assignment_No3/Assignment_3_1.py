def add(No):
    result=sum(No)
    return result


def main():

    print("Number Of List :- ")
    size=int(input())

    Data=list()
   
    print("Input Elents :-")
    for i in range(size):
        no=int(input())
        Data.append(no)

    print("Enterd Elemets are :-")
    for value in Data:
        print(value)

    ans=add(Data)
    print("Addition is:-",ans)
        
    


if __name__ == "__main__":
    main()