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

    df['Gender'] = ['Male','Male','Female']
    print(df)
    print(line)

    encode = pd.get_dummies(df, columns=['Gender'],prefix='Gender')
    print(encode)


if __name__ == "__main__":
    main()
