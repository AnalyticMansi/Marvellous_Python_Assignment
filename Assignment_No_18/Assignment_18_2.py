def main():
    filename = input("Enter the file name: ")

    fobj = open(filename, "r")
    data = fobj.read()
    fobj.close()

    print("\n--- File Content ---")
    print(data)

if __name__ == "__main__":
    main()
