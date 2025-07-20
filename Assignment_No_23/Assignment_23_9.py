import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

def main():

    data = {'Name':['Amit','Sagar','Pooja'],
    'Math':[np.nan,90,78], 
    'Science':[92,np.nan,80],
    'English':[75,85,82]}

    line = "*"*50

    df = pd.DataFrame(data)
    print(df) 
    print(line)


    df['Math'] = df['Math'].fillna(df['Math'].mean())
    df['Science'] = df['Science'].fillna(df['Science'].mean())
    print(line)
    print(df)







if __name__ == "__main__":
    main()
