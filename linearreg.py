from sklearn.linear_model import LinearRegression
import random
import matplotlib.pyplot as plt
import numpy as np

#Create Two empty list
feature_set = []
target_set = []

#Get the number of rows
number_of_rows = 200

#Limit the data possible values in the dataset
random_number_limit = 2000

#Create the dataset
#Create the feature dataset
for i in range(0, number_of_rows):
	x = random.randint(0, random_number_limit)
	y = random.randint(0, random_number_limit)
	z = random.randint(0, random_number_limit)

	# Creat a linear function for the target dataset
	function = (10*x)+(2*y)+(3*z)

	# Append the data to the list
	feature_set.append([x,y,z])
	target_set.append(function)

# plt.figure(1)
# plt.plot(feature_set, color='b')
# plt.plot(target_set, color='r')
# plt.show()

# Linear Regression model
model = LinearRegression()
model.fit(feature_set, target_set)

#test set
test_set = [[8, 10, 0]] 
prediction = model.predict(test_set)
print('Prediction:'+str(prediction)+' Coefficients:'+str(model.coef_))
