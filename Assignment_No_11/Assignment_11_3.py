sumd = 0

def fun(n):
    global sumd
    if n == 0:
        return
    sumd = sumd + (n % 10)
    fun(n // 10)

def main():
    num = 1234
    fun(num)
    print("Sum of digits is:", sumd)

if __name__ == "__main__":
    main()
