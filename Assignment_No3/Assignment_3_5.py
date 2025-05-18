# main.py
from MarvellousNum import ChkPrime

def ListPrime():
    print("Enter number of elements :-")
    size = int(input())

    Data = []

    print("Enter elements :- ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input elements are :- ")
    for value in Data:
        print(value)

    total = 0
    for value in Data:
        if ChkPrime(value):
            total += value

    return total

    
if __name__ == "__main__":
    result = ListPrime()
    print("Sum of prime numbers is:", result)
