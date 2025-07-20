import pandas as pd 
import numpy as np


def Missingvalue():
    
    data = {'Marks':[85,np.nan,90,np.nan,95]}


    line = "*"*50

    df = pd.DataFrame(data)
    print(df) 
    print(line)

    df['Marks'] = df['Marks'].interpolate(method='linear')
    print(df)



    

def main():
    
    Missingvalue()
   

if __name__ == "__main__":
    main()
