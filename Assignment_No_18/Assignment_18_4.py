import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py <file1> <file2>")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    
    f1 = open(file1, "r")
    data1 = f1.read()
    f1.close()

    
    f2 = open(file2, "r")
    data2 = f2.read()
    f2.close()

    
    if data1 == data2:
        print("Success: Both files have the same content.")
    else:
        print("Failure: Files have different content.")

if __name__ == "__main__":
    main()
