def ChkPN(value):
    No = 0

def main():
    print("Enter Any Number :- ")      # check no id positive negative and zero
    No = int(input())

    if(No>0):
        print("Positive Number")
    elif(No<0):
        print("Negative Number")
    else:
        print("Zero")

    ChkPN(No)

if __name__ == "__main__":
    main()