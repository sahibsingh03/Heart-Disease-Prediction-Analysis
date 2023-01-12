from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('heart.csv')
x = df.drop(columns='target',axis=1)
y = df['target']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,stratify=y,random_state=2)
model = LogisticRegression()
model.fit(x_train, y_train)

def predict(age,sex,cp,trestbp,chol,fbp,restecg,thalach,exang,oldpeak,slope,ca,thall):
    input_data = (age,sex,cp,trestbp,chol,fbp,restecg,thalach,exang,oldpeak,slope,ca,thall)

# change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    return prediction

