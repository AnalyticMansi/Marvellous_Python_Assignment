class Circle:

    PI= 3.14
    def __init__(self):
        self.Redius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def __del__(self):
        print("Inside Disctroctor Method")

    def Accept(self):
        self.Redius = float(input("Enter The Redius Of Circle :- ")) 
 
    def CalculateArea(self):
        self.Area = Circle.PI * self.Redius *self.Redius
    
    
    def CalculateCircumference(self):
        self.Circumference = 2*Circle.PI * self.Redius
        
    
    def Display(self):
        print(" Redius of Circle:- ",self.Redius)
        print("Area of cirlce is:- ",self.Area)
        print("Circumference of cirlce is :-",self.Circumference)

        
        
def main():

    obj = Circle()

    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()



if __name__ =="__main__":
    main()