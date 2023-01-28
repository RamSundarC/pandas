from matplotlib import pyplot as plt
import pandas as pd

data=pd.read_csv('data.csv')


# print(data.describe())
# print(data.head())
# print(data.columns)
total=[]
name=[]
def get_total():
    for i in range(len(data)):
        total.append(data['tamil']+data['English']+data["maths"]+data["science"]+data["social"])
    return total

def get_name():
    for i in data:
        name.append(i)
        print(i)
    return name

# name=data["name"]
total=list(get_total())
name=list(get_name())


print(name)
## explain pie chart for the above data

