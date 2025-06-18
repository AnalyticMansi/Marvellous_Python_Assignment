result = 0

def fun(n):
    global result
    if n == 0:
        return
    result = result + n
    fun(n - 1)

def main():
    fun(5)
    print("Sum from 1 to 5 is:-",result)

if __name__ == "__main__":
    main()
