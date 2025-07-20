import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

def main():

    data = {'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78], 
    'Science':[92,88,80],
    'English':[75,85,82]}

    line = "*"*50

    df = pd.DataFrame(data)
    print(df) 
    print(line)

    df['Total'] = df['Math'] + df['Science'] + df['English']
    print(df)
    print(line)

 
    plt.bar(df['Name'], df['Total'], color='pink')

    plt.ylabel('Total Marks')
    plt.xlabel('student names')
    plt.title('Bar plot')
    plt.show()

if __name__ == "__main__":
    main()
