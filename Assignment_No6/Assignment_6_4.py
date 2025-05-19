#This program display factorial of any number means using user input

def main():

    No=int(input("Enter Any Number :- "))
    fact=1
    for i in range (1, No+1):
        fact = fact*i
    print("Factorial of",No,"is :-",fact)
       
if __name__ == "__main__":
    main()