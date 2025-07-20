import pandas as pd
import numpy as np

def SalaryInfo():

    data = {'Salary':[25000,27000,29000,31000,50000,100000]}
    df = pd.DataFrame(data)
    print(df)
    

    Q1 = df['Salary'].quantile(0.25)
    Q3 = df['Salary'].quantile(0.75)

    IQR = Q3-Q1

    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    print("********************************")

    outliers = df[(df['Salary'] < lower) | (df['Salary'] > upper)]
    print("Outlier is :- ")
    print(outliers)





def main():

    SalaryInfo()
    
if __name__ == "__main__":
    main()
