import pandas as pd 
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def Minmaxscalar():
    
    data = {'Age':[18,22,25,30,35]}

    line = "*"*50

    df = pd.DataFrame(data)
    print(df) 
    print(line)

    minimum = df['Age'].min()
    maximum = df['Age'].max()

    df['Normlize'] = (df['Age'] - minimum) / (maximum - minimum)
    print(df)


def main():
    
    Minmaxscalar()
   

if __name__ == "__main__":
    main()
