def main():
    print("Enter the number of students:")
    n = int(input())

    fobj = open("marks.txt", "w")

    for i in range(n):
        print(f"\nEnter data for student {i+1}:")
        name = input("Name: ")
        marks = input("Marks: ")
        fobj.writelines(name + " " + marks + "\n")

    fobj.close()

    print("\nStudents with marks > 75:")
    fobj = open("marks.txt", "r")
    for line in fobj:
        data = line.strip().split()
        if len(data) == 2:
            if int(data[1]) > 75:
                print(data[0], data[1])
    fobj.close()

if __name__ == "__main__":
    main()
