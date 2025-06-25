class Numbers:
    def __init__(self):
        self.value = int(input("Enter The Value :- "))

    def ChkPrime(self):
        if self.value <2:
            return False
        for i in range(2, self.value):
            if self.value % i == 0:
                return False
        return True
        

    def ChkPerfect(self):
        if self.SumFactors() == self.value:
            return True
        else:
            return False
    
        

    def Factors(self):
        print("Factors Are :- ")
        for i in range(1,self.value):
            if self.value % i ==0:
                print(i,end=" ")
        print()
    
    def SumFactors(self):
        total = 0 
        for i in range(1,self.value):
            if self.value % i ==0:
                total = total + i 
        return total


def main():

    obj= Numbers()

    obj.Factors()
    
    ret= obj.SumFactors()
    print("Sum oF Factors :- ",ret)

    ret = obj.ChkPrime()
    print("Is Prime :-",ret)

    ret = obj.ChkPerfect()
    print("Is Perfect :-",ret)

if __name__ =="__main__":
    main()