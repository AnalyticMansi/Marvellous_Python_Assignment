import os

def main():
    filename = input("Enter the file name: ")

    if os.path.isfile(filename):
        print("File exists in the current directory.")
    else:
        print("File does not exist in the current directory.")

if __name__ == "__main__":
    main()
