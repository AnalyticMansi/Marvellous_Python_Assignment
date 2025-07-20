import os
import sys

def main():

    Firstlfile = sys.argv[1]
    Secondfile = sys.argv[2]

    fobj = open("ABC.text","r")
    data1 = fobj.read()
    fobj.close()

    fobj2 = open("Demo.txt","r")
    data2 = fobj2.read()
    fobj2.close()

    if(data1 == data2):
        print("Succes")
    else:
        print("Failure")


if __name__ =="__main__":
    main()