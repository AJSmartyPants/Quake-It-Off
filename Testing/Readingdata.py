import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.naive_bayes import GaussianNB

# Load the dataset from the csv file using pandas
data = pd.read_csv("https://confrecordings.ams3.digitaloceanspaces.com/CreditCard_9820.csv")
#data.head(10)
print(data.head(10))

fraud = data[data['Class'] == 1]
valid = data[data['Class'] == 0]
outlierFraction = len(fraud)/float(len(valid))
print(outlierFraction) #outlier is the noise in the data (random/dummy values)
print('Fraud Cases: {}'.format(len(data[data['Class'] == 1])))
print('Valid Transactions: {}'.format(len(data[data['Class'] == 0])))
# dividing the X and the Y from the dataset
X = data.drop(['Class'], axis = 1)
Y = data['Class']
print(X.shape)
print(Y.shape)

X = X.values
y = Y.values

#Splitting the dataset
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)

n = 7
#train with KNN
KNN = KNeighborsClassifier(n_neighbors = n)
KNN.fit(X_train, y_train)
knn_yhat = KNN.predict(X_test)
print('Accuracy score of the K-Nearest Neighbors model is {}'.format(accuracy_score(y_test, knn_yhat)))
print('F1 score of the K-Nearest Neighbors model is {}'.format(f1_score(y_test, knn_yhat)))

gnb = GaussianNB()
gnb.fit(X_train, y_train)

# making predictions on the testing set
y_pred = gnb.predict(X_test)

# comparing actual response values (y_test) with predicted response values (y_pred)
from sklearn.metrics import f1_score
print('Accuracy score of the GaussianNB Neighbors model is {}'.format(accuracy_score(y_test, y_pred)))
print("Gaussian Naive Bayes model accuracy(in %):", f1_score(y_test, y_pred)*100)


from sklearn.metrics import classification_report
print(classification_report(y_test,knn_yhat))
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,knn_yhat))

#data.head(num) gets number of rows from the top
#data.tail(num) gets rows from the bottom
#data.shape shows how many rows and columns are in data
#data.isnull().sum() checks and gets all the null (missing) values in the columns
#data.dropna(['columnname'], inplace = True) drops values off parts permanently, without the first parameter it will drop everything and leave your data empty