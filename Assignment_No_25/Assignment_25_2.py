import pandas as pd
import numpy as np

def EmployeeData():

    data = {'Name':['A','B','C'],
    'Age':[21.0,22.0,23.0]}
    df = pd.DataFrame(data)

    print("Original Data :- ")
    print("****************************")
    print(df.dtypes)
    print("*******************************")

  
    df['Age'] = df['Age'].astype(int)
    print("Updated DataFrame :-")
    print("************************")
    print(df)
    print("**********************")


    print("Updated Data types :-")
    print("************************")
    print(df.dtypes)
    

    
def main():

    EmployeeData()
    
if __name__ == "__main__":
    main()
