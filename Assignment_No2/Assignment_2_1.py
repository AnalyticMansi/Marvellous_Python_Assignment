from Arithmatic1 import Add,Sub,Mult,Div
def main():
     
     No1 = int(input("Enter First Number :- "))
     No2 = int(input("Enter Second Number :- "))
     print("-----------------------------------")

     Addition = Add(No1,No2)
     print("Addition OF Two NUmbers is :- ",Addition)
     print("-----------------------------------------")

     Substarction = Sub(No1,No2)
     print("Substraction of Two Numbers is :-",Substarction)
     print("-------------------------------------------")

     Multiplication =Mult(No1,No2)
     print("Multiplication of Two Numbers is :-",Multiplication)
     print("------------------------------------------")

     Division = Div(No1,No2)
     print("Division of Two Numbers is :- ",Division)

if __name__ == "__main__":
    main()