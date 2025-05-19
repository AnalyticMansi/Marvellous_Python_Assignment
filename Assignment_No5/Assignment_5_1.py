# Addition Divison Multiplication Substractio code using module


from Arithmatic import Add,Sub,Mult,Div

def main():

    No1 = int(input("Enter First Number :- "))
    No2 = int(input("Enter Second Number :- "))

    Addition = Add(No1,No2)
    print("Sum:-",Addition)

    Substarction = Sub(No1,No2)
    print("Diffrence:-",Substarction)

    Multiplication = Mult(No1,No2)
    print("Product:-",Multiplication)

    Division = Div(No1,No2)
    print("Division:-",Division)

if __name__ == "__main__":
    main()