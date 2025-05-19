# This program Display square and cube of given number using lambda function
    
def main():

    Square = lambda No : (No*No)
    Cube = lambda No :(No**3) 

    No = int(input("Enter a number :- "))
    
    square = Square(No)
    print("Squre:" ,square)

    cube = Cube(No)
    print("Cube:",cube)



if __name__ == "__main__":
    main()