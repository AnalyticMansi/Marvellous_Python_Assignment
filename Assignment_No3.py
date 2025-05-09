def Add(Value1 ,Value2):
    result = Value1 + Value2
    return result

def main():

    print("Enter First Number :- ")
    No1 = int(input())

    print("Enter Second Number :- ")
    No2 = int(input())

    addition = Add(No1,No2)                         #addition of two numbers
    print("Addition of two numbers is :-",addition)


if __name__ == "__main__":
    main()