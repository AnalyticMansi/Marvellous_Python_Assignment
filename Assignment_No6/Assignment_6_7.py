# This Program Display maximum number between given range using user input
def main():
    number = []
    
    print("Enterd 5 elements :-")
    for i in range(5):
        No = int(input())
        number.append(No)


    print("Enter 5 elements are:", *number) 
    print("Maximum Number is :-",max(number))


if __name__ == "__main__":
    main()