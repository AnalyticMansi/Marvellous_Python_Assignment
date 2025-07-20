import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns



def PrePridictorKNN(Datapath):

    df = pd.read_csv(Datapath)

    line = "*"*50
    
    print(line)
    print("Data Sample is :-")
    print(df.head())
    print(line)

    print("Clean the dataset :-")
    print(line)

    df.drop(columns =['Unnamed: 0'],inplace=True)

    print("Updated data is :")
    print(df.head())
    print(line)

    print("Missing value in each column :-",df.isnull().sum())
    print(line)

    
    
    le = LabelEncoder()
    df['Whether'] = le.fit_transform(df['Whether'])     
    df['Temperature'] = le.fit_transform(df['Temperature'])  
    df['Play'] = le.fit_transform(df['Play'])   

    X = df[['Whether','Temperature']]
    Y = df['Play']


    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, Y_train)

   
    y_pred = model.predict(X_test)

   
    print("Accuracy:", accuracy_score(Y_test, y_pred))



    plt.figure(figsize =(8,6))
    sns.scatterplot(x=X_test['Whether'], y=X_test['Temperature'], hue=y_pred, palette='Set1')
    plt.title("Marvellous Whether Temperature Classifier")
    plt.xlabel("Whether (Encoded)")
    plt.ylabel("Temperature (Encoded)")
    plt.grid(True)
    plt.show()
    
    
def main():
    
   PrePridictorKNN ("PlayPredictor.csv")
    
   

if __name__ == "__main__":
    main()
