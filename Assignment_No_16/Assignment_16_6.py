import os

def main():
    print("Enter the source file name :- ")
    source_file = input()

    print("Enter the destination file name :- ")
    destination_file = input()

    if os.path.exists(source_file):
        fsrc = open(source_file, "r")
        content = fsrc.read()
        fsrc.close()

        fdest = open(destination_file, "w")
        fdest.write(content)
        fdest.close()

        print("File content copied successfully.")
    else:
        print("Source file does not exist.")

if __name__ == "__main__":
    main()
