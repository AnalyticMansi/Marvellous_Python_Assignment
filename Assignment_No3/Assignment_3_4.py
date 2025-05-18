def count(data,num):
    cnt=0
    for value in data:
        if value == num:
            cnt=cnt+1
    return cnt 

def main():

    print("Enter number of elements :-")
    size = int(input())

    Data=list()

    print("Enter elements :- ")
    for i in range(size):
        no=int(input())
        Data.append(no)

    print("input elements are :- ")
    for value in Data:
        print(value)
     
    No1=int(input("Search element is :- "))
    ans = count(Data,No1)
    print("Output:-",ans)
    


if __name__ == "__main__":
    main()