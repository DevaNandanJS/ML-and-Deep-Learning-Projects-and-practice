import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model 

df= pd.read_csv(r"C:\ML practice\canada_per_capita_income.csv")
plt.xlabel('year')
plt.ylabel('per capita income (US$)')   

reg= linear_model.LinearRegression()
reg.fit(df[['year']], df['per capita income (US$)'])

input_data= pd.DataFrame([['2020']], columns=['year'])

prediction = reg.predict(input_data)
print(prediction)

x= reg.coef_
y= reg.intercept_
print(x,y)
print( x*2020 + y)

plt.scatter(df['year'], df['per capita income (US$)'], color = 'red', marker = '+')
plt.plot(df['year'], reg.predict(df[['year']]), color = 'blue')
plt.show()