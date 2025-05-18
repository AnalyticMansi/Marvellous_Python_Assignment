
def factorial():
    fact=1
    for i in range(1,no+1):
        fact = fact * i
    return result


def main():

    
    no = int(input("Enter a number :- "))
    
    ans=factorial(no)
    print(ans)
    

if __name__ == "__main__":
    main()