import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

def main():

    df = pd.read_csv('student.csv')


    sns.boxplot(x='Name',y='English' , data=df)
    plt.title("Marvellous boxplot")
    plt.show()



if __name__ == "__main__":
    main()
