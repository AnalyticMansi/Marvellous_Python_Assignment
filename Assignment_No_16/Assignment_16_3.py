import os


def main():

    print("Enter the file name :-")
    FileName = input()

    fobj = open(FileName,"r")
    data = fobj.read()
    fobj.close()

    lines = data.splitlines()
    words = data.split()
    char = len(data)

    print()   


if __name__ =="__main__":
    main()