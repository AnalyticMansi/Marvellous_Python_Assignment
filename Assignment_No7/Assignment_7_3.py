# this program display even number of given list using lambda funtion also used filter
def main():

    EvenNo = lambda No :(No%2==0)

    Data = [1,2,3,4,5,6]
    print("Input Data",Data)

    FData=list(filter(EvenNo,Data))
    print("Even Numbers :-",FData)
        
 
if __name__ =="__main__":
    main()