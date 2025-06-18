i=1
def fun():
    global i
    if i>5:
        return
    print(i,end=" ")
    i = i+1
    fun()

def main():
    fun()

if __name__ =="__main__":
    main()
