import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python program.py <source_filename>")
        return

    source_file = sys.argv[1]
    destination_file = "demo.txt"

    # Open source file and read content
    fsrc = open(source_file, "r")
    content = fsrc.read()
    fsrc.close()

    # Write content to demo.txt
    fdest = open(destination_file, "w")
    fdest.write(content)
    fdest.close()

    print(f"Contents copied from {source_file} to {destination_file}")

if __name__ == "__main__":
    main()
