# Check the largest number between 3 value

def main():
    value1 = int(input("Enter Fisrt Number :- "))
    value2 = int(input("Enter Second Number :- "))
    value3 = int(input("Enter Third Number :- "))

    if(value1>value2):
        print("Largest No is :- ",value1)
    elif(value2>value3):
        print("Largest No is :- ",value2)
    elif(value3>value1):
        print("Largest No is :-",value3)
        

if __name__ == "__main__":
    main()