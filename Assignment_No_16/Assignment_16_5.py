import os

def main():
    print("Enter File Name :- ")
    file_name = input()

    fobj = open(file_name, "w")

    print("Enter multiple lines (type 'exit' to stop):")
    while True:
        dat = input()
        if dat.lower() == "exit":
            break
        fobj.writelines(dat + "\n")
    fobj.close()

    ret = os.path.exists(file_name)
    if ret == True:
        print("File is present in directory")
        fobj = open(file_name, "r")
        print("Lines with more than 5 words:")
        for line in fobj:
            words = line.strip().split()
            if len(words) > 5:
                print(line.strip())
        fobj.close()
    else:
        print("File not found")

if __name__ == "__main__":
    main()
