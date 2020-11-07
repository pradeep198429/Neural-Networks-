# -*- coding: utf-8 -*-
"""Copy of Copy of neural_network_classification_forestfire_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VDxhXL6ySXcRWK-Og8GAZLrskmo49Tpw
"""

import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv("sample_data/forestfires.csv")


#df_new=pd.get_dummies(df,columns={'month','day','size_category'},drop_first=True)
#print(df_new)
df.drop(['month','day'], axis=1,inplace=True)
df['size_category'].replace({"small": 0,"large" : 1},inplace=True)
df.info()

X = df.drop('size_category',axis=1).values
y = df['size_category'].values

import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(x='size_category',data=df)
plt.show()
# to check class imbalance 


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=101)

from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state = 2) 
X_train_res, y_train_res = sm.fit_sample(X_train, y_train)
X_train_res.shape,y_train_res.shape

X_train=X_train_res.copy()
y_train=y_train_res.copy()

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

"""```
# This is formatted as code
```
"""

import keras
from keras.models import Sequential
from keras.layers import Dense 
from keras.layers import LeakyReLU,PReLU,ELU
from keras.layers import Dropout

model = Sequential()

model.add(Dense(units=17,activation='relu'))
model.add(Dense(units=17,activation='relu'))

model.add(Dense(units=1,activation='sigmoid'))


# For a binary classification problem
model.compile(loss='binary_crossentropy', optimizer='adam')

model.fit(x=X_train, 
          y=y_train, 
          epochs=600,
          validation_data=(X_test, y_test), verbose=1
          )
y_pred = model.predict_classes(X_test)

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report

print(confusion_matrix(y_test,y_pred))

print(accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))