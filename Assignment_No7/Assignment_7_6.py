# this program display prime no using filter 

def prime(No):
    if No == 2:
        return True
    if No % 2 == 0:
        return False
    for i in range(3, No // 2 + 1, 2):
        if No % i == 0:
            return False
    return True

def main():
    
    Data = [11,12,13,14,15,16,17]
    print("Input List :-",Data)

    FData = list(filter(prime,Data))
    print("Filter output :-",FData)



if __name__ =="__main__":
    main()