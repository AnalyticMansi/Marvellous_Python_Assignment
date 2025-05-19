 # This program display multiplication table of any number means uing user input
def main():
    i=1
    No = int(input("Enter Any Number :- "))
    
    while(i<=10):
        result = No*i
        i=i+1
        print(No,"*",i-1,"=",result)
        

if __name__ == "__main__":
    main()