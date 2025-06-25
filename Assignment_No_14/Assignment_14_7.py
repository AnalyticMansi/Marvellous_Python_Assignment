class Person:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age


class Teacher(Person):
    def __init__(self,name,age ,subject , salary):
        super().__init__(name,age)
        self.Subject = subject
        self.Salary = salary

    def Display(self):
        print("Name is :- ",self.Name)
        print("Age is :- ",self.Age)
        print("Subject is :- ",self.Subject)
        print("Salary is :- ",self.Salary)

def main():

    obj = Teacher("Mansi",23,"Math",50000)
    obj.Display()

if __name__ =="__main__":
    main()