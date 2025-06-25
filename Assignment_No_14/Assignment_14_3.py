class Book:
    def __init__(self,price):
        self.__Price = price  # Private 
    
    def set(self,p):
        self.__Price = p
    
    def get(self):
        return self.__Price


def main():

    obj = Book(450)

    print("Initial Price :-",obj.get())


    obj.set(500)
    print("Updated Price :-",obj.get())

if __name__ =="__main__":
    main()