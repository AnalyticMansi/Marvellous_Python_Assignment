import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


def main():

    data = {'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78], 
    'Science':[92,88,80],
    'English':[75,85,82]}

    line = "*"*50

    df = pd.DataFrame(data)
    print(df) 
    print(line)

    minimum = df['Math'].min()
    maximum = df['Math'].max()

    df['Normlized'] = (df['Math'] - minimum) / (maximum - minimum)
    print(df)

    
    
    
    #scaler = MinMaxScaler()
    #scale = ['Math']
    #df[scale] = scaler.fit_transform(df[scale])
    #print(df)


    



if __name__ == "__main__":
    main()
