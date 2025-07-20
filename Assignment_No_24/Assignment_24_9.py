import pandas as pd
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

    a = df.rename(columns={'Math':'Mathamatics'})
    print(a)



if __name__ == "__main__":
    main()
