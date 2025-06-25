class Student:

    school_name = "Pawar Public School"

    def __init__(self,name,roll_no):
        self.Name = name
        self.Roll_No = roll_no

    def Display(self):
        print("Schoool Name :- ",Student.school_name)
        print("Student Name is :-",self.Name)
        print("Student Roll No is :-",self.Roll_No)
    

def main():

    stud_info1 = Student("Mansi",101)
    stud_info2 = Student("Sayali",102)

    stud_info1.Display()
    print("-----------------------------")
    stud_info2.Display()
    print("-----------------------------")

    Student.school_name = "Podar International School"
     
    print("After Change The School Name :-")
    print("-----------------------------")
    stud_info1.Display()
    print("-----------------------------")
    stud_info2.Display()
    

if __name__ =="__main__":
    main()