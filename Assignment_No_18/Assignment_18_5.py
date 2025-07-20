def main():
    filename = input("Enter the file name: ")
    search_word = input("Enter the word to search: ")

    fobj = open(filename, "r")
    data = fobj.read()
    fobj.close()

    count = data.count(search_word)

    print(f"The word '{search_word}' appears {count} times in the file.")

if __name__ == "__main__":
    main()
