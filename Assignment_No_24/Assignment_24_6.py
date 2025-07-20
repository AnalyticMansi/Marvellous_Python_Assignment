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

    df['Total'] = df['Math'] + df['Science']+df['English']
    
   
    df['Status'] = df['Total'].apply(lambda  x:'Pass' if x>=250 else 'Fail')
    print(df)

    a= df.value_counts('Status')
    print(a)


if __name__ == "__main__":
    main()
