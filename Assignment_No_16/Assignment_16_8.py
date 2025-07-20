def main():
    print("Enter the source file name:")
    source_file = input()

    print("Enter the new file name to save cleaned content:")
    new_file = input()

    fsrc = open(source_file, "r")
    fdest = open(new_file, "w")

    for line in fsrc:
        if line.strip() != "":
            fdest.write(line)

    fsrc.close()
    fdest.close()

    print("Blank lines removed and saved to", new_file)

if __name__ == "__main__":
    main()
