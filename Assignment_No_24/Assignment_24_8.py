import pandas as pd
import matplotlib.pyplot as plt


def main():

    data = {'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78], 
    'Science':[92,88,80],
    'English':[75,85,82]}

    line = "*"*50

    df = pd.DataFrame(data)
    print(df) 
    print(line)

    plt.hist(df['Math'], bins=10 ,color='skyblue',edgecolor = 'black')
    plt.xlabel=('Math')
    plt.ylabel = ('frequncy')
    plt.title("Marvellous Histrogram of Student")
    plt.show()



if __name__ == "__main__":
    main()
