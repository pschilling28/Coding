#Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Reading the dataset
dataset = pd.read_csv("C:/Users/schil/OneDrive/Documents/Coding/Pat-s-Code/Coding/Python/Multiple_Regression/bq-results-20220304-145905-99bo1tskk41u.csv")
dataset.head()

    #test1
#print(dataset)


#Data pre-processing

#print(dataset.shape)

    #checking for missing values
#print(dataset.isna().sum())

    #checking for duplicate rows
#print(dataset.duplicated().any())

    #checking for outliers - rename headings
#fig, axs = plt.subplots(3, figsize = (5,5))
#plt1 = sns.boxplot(dataset['amount'], ax = axs[0])
#plt2 = sns.boxplot(dataset['workloadDriverName'], ax = axs[1])
#plt3 = sns.boxplot(dataset['amount'], ax = axs[2])
#plt.tight_layout()
#plt.show()

#Exploratory data analysis - rename heading

    #Distribution of the target variable
#sns.displot(dataset['amount'])
#plt.show()

    #Variable relationships - scatterplots - change headings
    #sns.pairplot(dataset, x_vars=['amount', 'Average Ticket', 'Items'], y_vars='workloadDriverName', height=4, aspect=1, kind='scatter')
sns.pairplot(dataset, x_vars=['amount'], y_vars='workloadDriverName', height=4, aspect=1, kind='scatter')
plt.show()

    #Heatmap
sns.heatmap(dataset.corr(), annot = True)
#plt.show()

#Model building

    #1. Simple linear regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics    

        #Setting the value for X and Y - replace with needed headings
x = dataset[['Average Ticket']].values
y = dataset['WH'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)

slr = LinearRegression()  
slr.fit(x_train, y_train)

        #Printing the model coefficients
#print('Intercept: ', slr.intercept_)
#print('Coefficient:', slr.coef_)

        #Print regression equation - replace variable names and placeholders for intercept and coefficient
#print("Regression equation: [Variable Y] = " + str(slr.intercept_) + " + " + str(slr.coef_) + " * [Variable X]")

        #Line of best fit replace with regression equation
plt.scatter(x_train, y_train)
plt.plot(x_train, 202.65 + 9.97*x_train,'r')
#plt.show()

        #Prediction of Test and Training set result  
y_pred_slr= slr.predict(x_test)  
x_pred_slr= slr.predict(x_train)
#print("Prediction for test set: {}".format(y_pred_slr))

        #Actual value and the predicted value
slr_diff = pd.DataFrame({'Actual value': y_test, 'Predicted value': y_pred_slr})
#print(slr_diff)

        #Predict for any value - replace predict value with chosen value: Read as "The model predicts the Y value of 10.003 for X"
#print(slr.predict([[56]]))

        # print the R-squared value for the model - Read R-squared % of the data fits the model
from sklearn.metrics import accuracy_score
#print('R squared value of the model: {:.2f}'.format(slr.score(x,y)*100))

        #0 means the model is perfect. Therefore the value should be as close to 0 as possible
meanAbErr = metrics.mean_absolute_error(y_test, y_pred_slr)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_slr)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_slr))

#print('Mean Absolute Error:', meanAbErr)
#print('Mean Square Error:', meanSqErr)
#print('Root Mean Square Error:', rootMeanSqErr)

    #2.Multiple linear regression

        #Setting the value for X and Y - replace with needed headings
x = dataset[['Average Ticket', 'Customer', 'Items']].values
y = dataset['WH'].values

x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.3, random_state=100) 

mlr= LinearRegression()  
mlr.fit(x_train, y_train) 

        #Printing the model coefficients
#print(mlr.intercept_)

        #pair the feature names with the coefficients
#print(list(zip(x, mlr.coef_)))

        #Predicting the Test and Train set result 
y_pred_mlr= mlr.predict(x_test)  
x_pred_mlr= mlr.predict(x_train)

#print("Prediction for test set: {}".format(y_pred_mlr))

        #Actual value and the predicted value
mlr_diff = pd.DataFrame({'Actual value': y_test, 'Predicted value': y_pred_mlr})
#print(mlr_diff)

        #Predict for any value set - replace predict value with chosen value: Read as "The model predicts the Y value of 10.003 for variables x1, x2, x3"
#print(mlr.predict([[56, 55, 67]]))

        #print the R-squared value for the model - Read R-squared % of the data fits the model
#print('R squared value of the model: {:.2f}'.format(mlr.score(x,y)*100))

        #0 means the model is perfect. Therefore the value should be as close to 0 as possible
meanAbErr = metrics.mean_absolute_error(y_test, y_pred_mlr)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_mlr)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_mlr))

#print('Mean Absolute Error:', meanAbErr)
#print('Mean Square Error:', meanSqErr)
#print('Root Mean Square Error:', rootMeanSqErr)