
def star():
    pass
    


def main():
    rows = 5
    cols=5
   

    for i in range (1,rows+1):
        for j in range (1,cols+1):
            print(" * ",end=" ")
        print()

    star()


if __name__ == "__main__":
    main()