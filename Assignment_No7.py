def Divisible(value):
    No = 0

def main():
    print("Enter Any Number :- ")   #check number is divisible by 5
    No = int(input())

    if(No%5==0):
        print("True")
    else:
        print("False")
   
    Divisible(No)

if __name__ == "__main__":
    main()