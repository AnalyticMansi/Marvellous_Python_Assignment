import pandas as pd
import numpy as np

def main():
    
    data = {'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78], 
    'Science':[92,88,80],
    'English':[75,85,82]}

    line = "*"*50

    df = pd.DataFrame(data)
    print(df) 
    print(line)

    print("Shape(row and column) of the dataset :-")
    print(df.shape)
    print(line)

    print("Columns in datasets :-")
    print(df.columns)
    print(line)

    print("Data Type of the dataframe :-")
    print(df.info())
    print(line)   

if __name__ == "__main__":
    main()
