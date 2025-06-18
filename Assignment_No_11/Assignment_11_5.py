count = 0

def fun(n):
    global count
    if n == 0:
        return
    if n % 10 == 0:
        count = count + 1
    fun(n // 10)

def main():
    num = 1020300
    fun(num)
    print("Count of zeros is:",count)

if __name__ == "__main__":
    main()
