class Product:
    def __init__(self,name,price):
        self.Name = name
        self.Price = price
    
    def __eq__(self,other):
        return self.Price == other.Price

def main():

    p1 = Product("Laptop",50000)
    p2 = Product("Mobile",50000)

    if p1==p2:
        print("Both products have the same price ")
    else:
        print("Product have diffrent prices")

if __name__ =="__main__":
    main()