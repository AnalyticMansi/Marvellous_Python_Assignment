import threading

def odd():
    for i in range(1,20,2):
        print(i)
    return

def even():
    for i in range(2,22,2):
        print(i)
    return


def main():

    T1=threading.Thread(target = odd)
    T2=threading.Thread(target = even)


    T1.start()
    T2.start()

    T1.join()
    T2.join()



if __name__ == "__main__":
    main()