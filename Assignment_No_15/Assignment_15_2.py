import os

def main():

    print("Enter the name of file that you want to read :-")
    FileName =input()


    fobj = open(FileName,"w")

    print("Enter the data you want to write ")
    data = input()
    fobj.write(data)


    ret = os.path.exists(FileName)


    if(ret==True):
        print("File is present in current direcotry")
        fobj = open(FileName,"r")
        data = fobj.read()

        print("Data from file is :-",data)

        fobj.close()
        
    else:
        print("File is not Exists.....")


if __name__ =="__main__":
    main()