import pandas as pd
import numpy as np

"""
from sklearn.datasets import load_boston

boston_dataset= load_boston()

boston_df= pd.DataFrame(boston_dataset.data, columns= boston_dataset.feature_names)
"""
#print(boston_df.head())


###csv file to pands df

diabetes_df= pd.read_csv(r"C:\ML practice\datasets\diabetes.csv")

#print(diabetes_df.head())

#df to csv

diabetes_df.to_csv("diabetes_df.csv")



### making random df

random_df= pd.DataFrame(np.random.rand(20,10))
#print(random_df.head())
"""
print(diabetes_df.info())
print(diabetes_df.isnull().sum())
print(diabetes_df.describe())
print(diabetes_df.corr())
"""


###counting the values based on label
"""
print(diabetes_df.value_counts("Outcome"))

print(diabetes_df.mean())
print(diabetes_df.std())
"""

###alll statistical measures in one go 

print(diabetes_df.describe())



### Manipulating the data frame

#boston_df['price']= boston_dataset.target 

#removing row
diabetes_df.drop(index=0, axis=0) #index is index number of row and axis determines wether its a row or column (0= row, column= 1)

#removing column
diabetes_df.drop(columns= "Age", axis= 1)

#locating row using index value
diabetes_df.iloc[0]  #locates first row

#locating column
diabetes_df.iloc[:,0] #locates first column

