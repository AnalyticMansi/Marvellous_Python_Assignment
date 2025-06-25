class BookStore:

    NoOfBooks = 0

    def __init__(self,name,author):
        self.Name = name
        self.Author = author

        BookStore.NoOfBooks = BookStore.NoOfBooks + 1
        

    def Display(self):
        print(self.Name,"by ",self.Author,".No of Book:",BookStore.NoOfBooks)
        
        


def main():

    obj1 = BookStore("Linux System Programming","Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming","Denis Rechie")
    obj2.Display()
    

if __name__ =="__main__":
    main()