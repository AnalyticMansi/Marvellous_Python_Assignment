def SumAdd(value):
    pass


def main():
    
    no = int(input("Enter a number:- "))
    sum=0
    while (no>0):
        sum+=no%10
        no//=10
    print(sum)

if __name__ == "__main__":
    main()