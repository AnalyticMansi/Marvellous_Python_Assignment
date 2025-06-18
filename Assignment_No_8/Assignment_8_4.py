import threading 

def small(text):
    cnt =0
    for char in text:
        if char.islower():
            cnt = cnt+1
    print("Small Letters in String are :-",cnt) 


def capital(text):
    cnt =0
    for char in text:
        if char.isupper():
            cnt= cnt+1
    print("Capital Letters in string are :-",cnt)

def digits(text):
    cnt =0
    for char in text:
        if char.isdigit():
            cnt=cnt+1
    print("Digits in String are :-",cnt)



def main():

    name = input("Enter The String :- ")
    

    T1 = threading.Thread(target = small ,args=(name,))
    T2 = threading.Thread(target= capital , args=(name,))
    T3 = threading.Thread(target = digits , args=(name,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()





if __name__ == "__main__":
    main()
