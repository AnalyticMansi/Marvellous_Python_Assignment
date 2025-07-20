import os


def main():


    print("Enter 10 numbers:-")

    numbers =[]

    for i in range(10):
        num = input(f"Enter Number :- " )
        numbers.append(num + "\n")

    fobj = open("number.txt","w")
    fobj.writelines(numbers)
    fobj.close() 


if __name__ =="__main__":
    main()