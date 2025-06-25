class Demo:

    ClassValue = "Value"

    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B

    def Fun(self):
        result = 0
        result = self.no1 + self.no2
        return result

    def Gun(self):
        result = 0
        result = self.no1 + self.no2
        return result


def main():

    print("Class Variable :-"+Demo.ClassValue)

    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    ret = obj1.Fun()
    print(" This is Fun value of object first:-",ret)

    ret = obj2.Fun()
    print(" This is Fun value of object Second:-",ret)

    ret = obj1.Gun()
    print(" This is Gun value of object first:-",ret)

    ret = obj2.Gun()
    print(" This is Gun value of object Second:-",ret)


if __name__ =="__main__":
    main()
