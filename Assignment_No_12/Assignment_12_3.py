class Arithmatic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def __del__(self):
        print("Inside Distroctor Method")

    def Accept(self):
        self.value1 = int(input("Enter First Value :- "))
        self.value2 = int(input("Enter Second Value :- "))

    def Addition(self):
        ans = 0
        ans = self.value1 + self.value2
        return ans

    def Substraction(self):
        ans = 0
        ans = self.value1 - self.value2
        return ans

    def Multiplication(self):
        ans = 0 
        ans = self.value1 * self.value2
        return ans

    def Division(self):
        ans = self.value1 / self.value2
        return ans

def main():

    obj = Arithmatic()

    obj.Accept()

    ret = obj.Addition()
    print("Addition is :- ",ret)

    ret = obj.Substraction()
    print("Substraction is :-",ret)

    ret = obj.Multiplication()
    print("Miltiplication is :-",ret)

    ret = obj.Division()
    print("Division is :-",ret)


if __name__ =="__main__":
    main()