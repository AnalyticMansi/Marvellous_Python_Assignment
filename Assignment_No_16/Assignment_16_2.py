
import os 

def main():

    print("Enter the file name you want to create :-")
    FileName = input()

    fobj = open(FileName,"w")

    print("Enter the data you want add in file ")
    write_data = input()

    fobj.writelines(write_data)
    fobj.close()

    ret = os.path.exists(FileName)
    if(ret==True):
        
        print("File is present in current direcotry")
        fobj = open(FileName,"r")
        data = fobj.read()

        print("Data from file is :-",data)

        fobj.close()

    else:
        print("There is no such file")


if __name__ =="__main__":
    main()