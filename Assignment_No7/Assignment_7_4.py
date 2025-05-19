# this program display product of all numbers using lambda function

from functools import reduce
def main():

    Product = lambda A,B:(A*B)

    Data =[2,3,4]
    print("Input Elements :-",Data)

    RData = reduce(Product,Data)
    print("Product :-",RData)


if __name__=="__main__":
    main()