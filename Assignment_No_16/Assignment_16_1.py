
def main():

    print("Enter the file name you want to create :-")
    FileName = input()

    fobj = open(FileName,"w")

    print("Enter the data ypu want to write :-")
    data = input()

    fobj.writelines(data)
    fobj.close()


if __name__ =="__main__":
    main()