class Calculator:
    def __init__(self):
        self.value1 = int(input("Enter First Value :- "))
        self.value2 = int(input("Enter Second Vavlue :- "))

    def add(self):
        Addition = self.value1 + self.value2
        print("Addition is :-",Addition)

    def sub(self):
        Substarction = self.value1 - self.value2
        print("Substraction is :- ",Substarction)
    
    def mul(self):
        Multiplication = self.value1 * self.value2
        print("Multiplication is :-",Multiplication)

    def div(self):
        Division = self.value1 / self.value2
        print("Division is :-",Division)


def main():

    obj = Calculator()

    obj.add()
    print("----------------------------")
    obj.sub()
    print("----------------------------")
    obj.mul()
    print("----------------------------")
    obj.div()

if __name__ =="__main__":
    main()