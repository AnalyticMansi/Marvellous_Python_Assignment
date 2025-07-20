import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split



def SupervisedLearning():
    
    data = data = {
    'Age': [22, 30, 45, 35, 22],
    'Salary': [50000, 60000,80000,65000,45000],
    'Purchased': [1,0,1,0,1]}


    line = "*"*50

    df = pd.DataFrame(data)
    print(df) 
    print(line)


    X = df[['Age', 'Salary']]        
    y = df['Purchased']             

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Display results
    print("X_train:", X_train)
    print(line)
    print("X_test:", X_test)
    print(line)
    print("y_train:", Y_train)
    print(line)
    print("y_test:", Y_test)

    
def main():
    
    SupervisedLearning()
    
   

if __name__ == "__main__":
    main()
