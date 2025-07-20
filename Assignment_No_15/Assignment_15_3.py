import os
import sys

def main():

    Targetfile = sys.argv[1]

    sourcefile = "Demo.txt"

    if os.path.exists(sourcefile):
        print("File is found")

        fobj = open(sourcefile,"r")
        data = fobj.read()
        fobj.close()

        fobj2 = open(Targetfile,"w")
        fobj2.write(data)
        fobj2.close()

        print("Content copy successfully")
    else:
        print("File dose not exits")


if __name__ =="__main__":
    main()