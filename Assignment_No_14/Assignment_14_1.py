class Employee:
    def __init__(self,A,B,C):
        self.Name = A
        self.Emp_Id = B
        self.Salary = C

    

def main():
    
    obj = Employee("Mansi","101","40000")
    
    print("Employee Name :- " +obj.Name)
    print("Employee Name :- " +obj.Emp_Id)
    print("Employee Name :- " +obj.Salary)

if __name__ =="__main__":
    main()