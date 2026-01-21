import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

sonar_data= pd.read_csv(r'D:\ML practice\datasets\Copy of sonar data.csv', header=None)

"""
print(sonar_data.head())
print(sonar_data.shape)
print(sonar_data.describe())
"""

print(sonar_data[60].value_counts())
print(sonar_data.groupby(60).mean())

#seperating data and label
x= sonar_data.drop(columns=60, axis=1)       #dont consider the last row, which is the label
y= sonar_data[60]                            #just the label

#training and test data split
x_train, X_test, y_train, y_test= train_test_split(x, y, test_size=0.1, stratify=y, random_state=1) #test_size will determine size, statify will split based on the number of rock and mine(label=y), 

#Training

model= LogisticRegression()
model.fit(x_train, y_train)

x_train_prediction= model.predict(x_train)
x_test_prediction= model.predict(X_test)

training_data_accuracy= accuracy_score(x_train_prediction, y_train)
test_data_accuracy= accuracy_score(x_test_prediction, y_test)

print(training_data_accuracy)
print(test_data_accuracy)


#Predictive system

input_data_str= input("enter your data: ")
input_data_list = input_data_str.split(',')
input_data_float = [float(x) for x in input_data_list]
input_data_np= np.asarray(input_data_float)

#reshape numpy array as we are predicting for 1 instance
input_data_reshaped= input_data_np.reshape(1,-1)
prediction= model.predict(input_data_reshaped)
print(prediction)

if prediction[0]== 'R':
    print("Rock")
else:
    print("Mine")


#input
# R= 0.0200,0.0371,0.0428,0.0207,0.0954,0.0986,0.1539,0.1601,0.3109,0.2111,0.1609,0.1582,0.2238,0.0645,0.0660,0.2273,0.3100,0.2999,0.5078,0.4797,0.5783,0.5071,0.4328,0.5550,0.6711,0.6415,0.7104,0.8080,0.6791,0.3857,0.1307,0.2604,0.5121,0.7547,0.8537,0.8507,0.6692,0.6097,0.4943,0.2744,0.0510,0.2834,0.2825,0.4256,0.2641,0.1386,0.1051,0.1343,0.0383,0.0324,0.0232,0.0027,0.0065,0.0159,0.0072,0.0167,0.0180,0.0084,0.0090,0.0032
# M= 0.1088,0.1278,0.0926,0.1234,0.1276,0.1731,0.1948,0.4262,0.6828,0.5761,0.4733,0.2362,0.1023,0.2904,0.4713,0.4659,0.1415,0.0849,0.3257,0.9007,0.9312,0.4856,0.1346,0.1604,0.2737,0.5609,0.3654,0.6139,0.5470,0.8474,0.5638,0.5443,0.5086,0.6253,0.8497,0.8406,0.8420,0.9136,0.7713,0.4882,0.3724,0.4469,0.4586,0.4491,0.5616,0.4305,0.0945,0.0794,0.0274,0.0154,0.0140,0.0455,0.0213,0.0082,0.0124,0.0167,0.0103,0.0205,0.0178,0.0187