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

    sagar = df[df['Name'] == 'Sagar']
    marks = [sagar['Math'].values[0] , sagar['Science'].values[0],sagar['English'].values[0]]
    subject = ['Math','Science','English']

    plt.pie(marks,labels=subject , autopct='%1.1f%%')
    plt.title("Marks Distribution")
    plt.show()



if __name__ == "__main__":
    main()
