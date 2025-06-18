def Display(n, i=1):
    if i > n:
        return
    print("* " * i)
    Display(n, i + 1)

def main():
    Display(4)

if __name__ == "__main__":
    main()
