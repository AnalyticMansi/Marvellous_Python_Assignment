class Rectangle:
    def __init__(self,A,B):
        self.length = A
        self.width = B
    
    def CalculateArea(self):
        ans =0
        ans = self.length * self.width
        return ans

    def CalculatePerimeter(self):
        perimeter = 2 *(self.length + self.width)
        return perimeter


def main():

    obj = Rectangle(10,5)

    ret = obj.CalculateArea()
    print("Area is :-",ret)

    ret = obj.CalculatePerimeter()
    print("Perimeter is :-",ret)

if __name__=="__main__":
    main()