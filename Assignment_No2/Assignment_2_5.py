
def primeNo(no):
    if(no%no==0):
        if(no%2==0):
            print(" It is  Not Prime Number")
        else:
            print(" It is Prime Number")


def main():

    No = int(input("Enter a number :- "))
    ans=primeNo(No)
    
    

if __name__ == "__main__":
    main()