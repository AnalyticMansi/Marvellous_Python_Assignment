result = 1

def fun(x, y):
    global result
    if y == 0:
        return
    result = result * x
    fun(x, y - 1)

def main():
    fun(2, 3)
    print("Power of (2,3) is :- ",result)

if __name__ == "__main__":
    main()
