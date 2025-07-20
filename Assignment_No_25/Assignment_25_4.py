import pandas as pd


def EmployeeData():

    data ={'Department': ['HR','IT',  'Finance', 'HR','IT' ]}
    df = pd.DataFrame(data)
   
    encode = pd.get_dummies(df,columns=['Department'])
    print(encode)

    
def main():

    EmployeeData()
    
if __name__ == "__main__":
    main()
