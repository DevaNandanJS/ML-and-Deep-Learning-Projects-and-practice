import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df= pd.read_csv(r"C:\ML practice\datasets\insurance_data.csv")
print(df)

plt.scatter(df[['age']], df['bought_insurance'], color='red', marker='+')
plt.show()

print(df.shape)

x_train, x_test, y_train, y_test = train_test_split(df[['age']], df['bought_insurance'], test_size=0.1)
"""
print(x_train.shape)
print(x_test)
print(y_train.shape)
print(y_test.shape)
"""
model= LogisticRegression()

model.fit(x_train, y_train)

print(model.predict(x_test))

#print(model.score(x_test, y_test))