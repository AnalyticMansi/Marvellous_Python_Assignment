import pandas as pd
from sklearn.preprocessing import LabelEncoder

def EmployeeData():

    data = data = {'City': ['Pune','Mumbai',  'Delhi', 'Pune','Delhi' ]}
    df = pd.DataFrame(data)
   
    le = LabelEncoder()
    df['City'] = le.fit_transform(df['City'])


    print(df)

    
def main():

    EmployeeData()
    
if __name__ == "__main__":
    main()
