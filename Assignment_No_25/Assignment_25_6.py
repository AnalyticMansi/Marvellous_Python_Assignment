import pandas as pd
import numpy as np

def EmployeeData():

    data =  {'Grade': ['A+', 'B', 'A', 'C', 'B+']}
    df = pd.DataFrame(data)

    change = { 'A+':'Excellent',
    'B':'Avrage',
    'C':'Poor',
    'A':'Very Good',
    'B+':'Good'}
    print("***************************************")

    df['Grade'] = df['Grade'].replace(change)
    print(df)


   
def main():

    EmployeeData()
    
if __name__ == "__main__":
    main()
