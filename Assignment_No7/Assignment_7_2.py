#This program display double list of given list using lambda funtion and aslo map

def main():
    
    sum = lambda No:(No*2)
    
    Data = [1,2,3,4,5]
    print("Input Data:-" ,Data)


    MData = list(map(sum,Data))
    print("Double List ",MData)

if __name__ =="__main__":
    main()