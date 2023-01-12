import os
import numpy as np
import pandas as pd
import warnings
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
warnings.filterwarnings("ignore")
pd.set_option("display.max_rows",None)
from sklearn import preprocessing
import matplotlib
matplotlib.style.use('ggplot')
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv("heart.csv")
df.head()
#1
df.drop(['thall','caa'],axis=1,inplace=True)

df.dtypes
string_col=df.select_dtypes("string").columns.to_list()

num_col=df.columns.to_list()
#print(num_col)


df.info()
# Checking for NULLs in the data
df.isnull().sum()
#So we can see our data does not have any null values but in case we have missing values, we can remove the data as well.
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(df[['Weight']])
df['Weight'] = imputer.transform(df[['Weight']])