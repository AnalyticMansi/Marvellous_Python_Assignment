class Employee:
    def __init__(self,name,department,salary):
        self.Name = name                    #public
        self._Department = department       #protected
        self.__Salary = salary              #private

    def Display(self):
        print("Name is :- ",self.Name)
        print("Departemnt is :-",self._Department)
        print("Salary is :-",self.__Salary)

def main():

    obj = Employee("Mansi","IT",50000)

    obj.Display()

    print("Public (Name) is :- ",obj.Name)
    print("Protected (Departament) is ",obj._Department)
    print("Private (salary) is :-",obj._Employee__Salary)

if __name__ =="__main__":
    main()