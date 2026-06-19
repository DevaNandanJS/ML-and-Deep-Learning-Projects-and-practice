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
print(diabetes_dataset.shape)

# understanding the data, statistical measures
print(diabetes_dataset.describe())

x= diabetes_dataset.drop(columns= "Outcome", axis= 1)
y= diabetes_dataset["Outcome"]

