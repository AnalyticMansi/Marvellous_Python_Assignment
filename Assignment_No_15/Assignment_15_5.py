import os


def main():

    print("Enter the file name :-")
    FileName = input()

    print("Enter the word you want to search")
    search_word = input()


    fobj = open(FileName,"r")
    data = fobj.read()
    fobj.close()

    count1 = data.count(search_word)

    print(f"The word appears '{count1}' times in file")

    


if __name__ =="__main__":
    main()