class Vehicle:
    def start(self):
        print("Inside Vehicle Start")

class Car:
    def start(self):
        print("Inside Car Start")


def main():

    obj1 = Vehicle()
    obj2 = Car()

    obj1.start()
    obj2.start()

if __name__ =="__main__":
    main()