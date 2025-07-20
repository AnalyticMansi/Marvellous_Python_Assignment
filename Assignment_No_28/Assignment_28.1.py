import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt



def PrePridictorKNN(Datapath):

    df = pd.read_csv(Datapath)

    line = "*"*50
    
    print(line)
    print("Data Sample is :-")
    print(df.head())
    print(line)

    

    print("Missing value in each column :-",df.isnull().sum())
    print(line)

    
    
    X = df.drop('Class', axis=1)
    y = df['Class']               

        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)


    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train_scaled, y_train)


    y_pred = knn.predict(X_test_scaled)


    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    plt.figure(figsize=(8,6))
    sns.scatterplot(x=X['Alcohol'], y=X['Color intensity'], hue=y, palette='Set1', s=100)
    plt.title("Wine Classification: Alcohol vs Color Intensity")
    plt.xlabel("Alcohol")
    plt.ylabel("Color Intensity")
    plt.grid(True)
    plt.show()


        
    
def main():
    
   PrePridictorKNN ("WinePredictor.csv")
    
   

if __name__ == "__main__":
    main()
