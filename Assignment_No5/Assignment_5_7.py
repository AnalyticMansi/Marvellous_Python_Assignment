#program display area and perimeter of recatngle using user input

def main():
    length = int(input("Enter length of rectangle :- "))
    width = int(input("Enter Width of rectangle :- "))

    Area = length*width
    print("Area is :- ",Area)

    perimeter = 2 * (length + width)
    print("Perimeter :- ",perimeter)

if __name__ == "__main__":
    main()