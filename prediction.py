import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline

df=pd.read_csv("heart.csv")
df.head()

df.isnull().sum()

from sklearn.model_selection import train_test_split

x = df.drop(columns='target',axis=1)
y=df['target']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

model.fit(x_train,y_train)

model.score(x_test,y_test)
