import pandas as pd
from sklearn.model_selection import train_test_split


def EmployeeData():

    data = {
    'Age': [22, 25, 47, 52, 46, 56],
    'Purchased': [0, 1, 1, 0, 1, 0]}
    df = pd.DataFrame(data)
    print("*******************************")
   
    X = df['Age']
    Y = df['Purchased']

    X_train , X_test , Y_train ,Y_test = train_test_split(X,Y, test_size=0.2 , random_state=42)


    print("Training Features::-", X_train)
    print("*******************************")
    print("Training Labels:", Y_train)
    print("*******************************")
    print("Testing Features:", X_test)
    print("*******************************")
    print("Testing Labels:", Y_test)
    print("*******************************")
    
def main():

    EmployeeData()
    
if __name__ == "__main__":
    main()
