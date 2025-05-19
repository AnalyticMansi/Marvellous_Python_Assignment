# Chek [a,e,i,o,u] means check vowels are present or not 
def ChkVowel(No):
    pass
def main():

    value = input("Enter a character :- ")
    Data =  ["a","e","i","o","u"]
    
    for i in Data:
        if(i==value):
            print(i,"is vowel")

    ChkVowel(Data)
    

if __name__ == "__main__":
    main()