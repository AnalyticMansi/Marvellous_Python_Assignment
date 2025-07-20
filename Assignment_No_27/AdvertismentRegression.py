import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def MarvellousAdvertise(Datapath):

    df = pd.read_csv(Datapath)
    
    print("Dataset sample is :-")
    print(df.head())
   
    print("clean the dataset :- ")

    df.drop(columns=['Unnamed: 0'],inplace=True)

    print("updtaed dataset is :-")
    print(df.head())

    print("Missing value in each column :- ",df.isnull().sum())

    print("Statical summary :- ")
    print(df.describe())

    print("Correlation matrix")
    print(df.corr())


def main():

    MarvellousAdvertise("Advertising.csv")


if __name__ =="__main__":
    main()