import pandas as pd 
import numpy as np


def Replcaevalue():
    
    data = {'Marks':[45,67,88,32,76]}


    line = "*"*50

    df = pd.DataFrame(data)
    print(df) 
    print(line)
    
    df['Marks'] = df['Marks'].where(df['Marks'] >=50, 'Fail')
    print(df)
    
    

def main():
    
    Replcaevalue()
   

if __name__ == "__main__":
    main()
