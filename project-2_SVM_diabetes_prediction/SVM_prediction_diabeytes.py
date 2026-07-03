# importing libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score

#loading the dataset
diabetes_dataset= pd.read_csv(r"C:\ML-Practice-and-Projects\datasets\diabetes.csv")

#printing first 5 rows
print(diabetes_dataset.head())

# number of rows and columns
#print(diabetes_dataset.shape)

# understanding the data, statistical measures
#print(diabetes_dataset.describe())
x= diabetes_dataset.drop(columns="Outcome",axis= 1)
y= diabetes_dataset["Outcome"]

# Data standardization, to make it in a uniform range
scaler= StandardScaler()
scaler.fit(x) #fits the data into tha variable

standardized_data = scaler.transform(x)

x= standardized_data
y= diabetes_dataset["Outcome"]

# splitting the Data, train test split
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size=0.2, random_state= 2, stratify= y)

# TRAINING THE MODEL
classifier= svm.SVC(kernel= "linear")

#trainig the svm classifier
classifier.fit(x_train, y_train)

#Eval, Acuuracy score
X_train_accuracy= classifier.predict(x_train)
training_data_accuracy= accuracy_score(X_train_accuracy, y_train)

print(f"accuracy score of training data= {training_data_accuracy}")

Test_accuracy= classifier.predict(x_test)
test_accuracy_predict= accuracy_score(Test_accuracy, y_test)
print(f"accuracy score of data= {test_accuracy_predict}")

# Making a predictive system 
input_data = (1,85,66,29,0,26.6,0.351,31)

input_array= np.asanyarray(input_data)

#reshape the array as we are predicting for one instance 
input_data_reshaped= input_array.reshape(1, -1)

# Standardize the input data 
std_data= scaler.transform(input_data_reshaped)

prediction= classifier.predict(std_data)
print(prediction)
