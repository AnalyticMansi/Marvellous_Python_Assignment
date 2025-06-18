i = 1
fact = 1

def fun(n):
    global i, fact
    if i > n:
        return
    fact = fact * i
    i = i + 1
    fun(n)

def main():
    num = 5
    fun(num)
    print("Factorial is:-", fact)

if __name__ == "__main__":
    main()
