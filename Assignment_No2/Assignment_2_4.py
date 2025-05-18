
def SumFactors(no):
    total = 0
    for i in range(1, no):
        if no % i == 0:
            total += i
    return total

def main():
    num = int(input("Enter a number: "))
    result = SumFactors(num)
    print("Sum of factors is:", result)

if __name__ == "__main__":
    main()
