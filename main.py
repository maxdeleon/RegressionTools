import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model


balance_sheet = pd.read_csv('natGasData.csv')
balance_sheet.index = balance_sheet['Month']
balance_sheet.drop(['Month'], axis=1)
balance_sheet = balance_sheet.dropna()

#print(balance_sheet.columns)

residential_regression_y = balance_sheet['Residential Consumption']
electrical_regression_y = balance_sheet['Electric Power Consumption']

months = ['Feb','Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
trend = 'trend'
X = balance_sheet[months]
X = sm.add_constant(X)
Y = residential_regression_y


regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

predictions = regr.predict(X)


balance_sheet['res model'] = predictions






# Doesnt match up properly with teh excel sheet
ax = plt.gca()
balance_sheet.plot(y='Residential Consumption', color='blue', ax=ax, figsize=(10,5))
balance_sheet.plot(y='res model', color='red',style='--', ax=ax)
plt.ylabel('Nat gas Usage (Bcf)')
#save plot
plt.savefig('plot.png')
plt.show(figsize=(20,7))




