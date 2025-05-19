# this program disaply given string is pallindrome or not

def main():

    char =input("Enter Any Name :- ")

    rev=""

    for i in char:
        rev=rev+i
    
    if (rev==char):
        print(char," is pallindrome")
    else:
        print("Not Pallindrome")

    
        

if __name__ =="__main__":
    main()