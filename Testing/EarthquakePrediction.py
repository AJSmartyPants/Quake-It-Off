#Importing necessary packages, assets, and libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, r2_score
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.datasets import load_diabetes

#Setting the data, removing null values, and creating the label encoder
notimportantcols = ["Type", "Magnitude Type", "Magnitude Error", "Magnitude Seismic Stations", "Azimuthal Gap", "Horizontal Distance", "Horizontal Error", "ID", "Source", "Location Source", "Magnitude Source", "Status", "Depth Error", "Depth Seismic Stations", "Root Mean Square"]
le = LabelEncoder()
data = pd.read_csv("https://confrecordings.ams3.digitaloceanspaces.com/database.csv")
data = data[data["Type"].str.contains("Nuclear Explosion|Explosion|Rock Burst") == False]
data = data.drop(notimportantcols, axis = 1)

#Applying the label encoder and getting the number of cases for each type of weather for reference
print(data.columns)
print(data.shape)

import datetime

timestamp = []
for d, t in zip(data['Date'], data['Time']):
    try:
        if '/' in d:
            dt_format = '%m/%d/%Y %H:%M:%S'
        else:
            dt_format = '%m-%d-%Y %H:%M:%S'
        dt = datetime.datetime.strptime(d + ' ' + t, dt_format)
        dt_utc = dt.replace(tzinfo=datetime.timezone.utc)
        timestamp.append(int(dt_utc.timestamp()))
    except ValueError:
        timestamp.append('ValueError')

data['Timestamp'] = timestamp
print(data.head(10))
data = data.drop(["Date", "Time"], axis = 1)
print(data.head(10))
#data = data[data["Type"].str.contains("Nuclear Explosion|Explosion|Rock Burst") == False]
#cols = ['Date', 'Time']
#data[cols] = data[cols].apply(le.fit_transform)
data['Magnitude'] = data['Magnitude'].astype(str).str.replace('.', '')
data['Depth'] = data['Depth'].astype(str).str.replace('.', '')
data = data[data != 'ValueError']
#dtype = {"Cold":0, "Fog":1, "Hail":2, "Rain":3, "Snow":4, "Storm":5, "Precipitation":6}
#data["Type"] = data["Type"].map(dtype)
print(data.shape)
print(data.head(3))
data.dropna(inplace=True)

#Using train_test_split to create the model's training and testing: Testing size is 20% of the dataset
#inputcols = ["Type", "Magnitude Type", "Magnitude Error", "Magnitude Seismic Stations", "Azimuthal Gap", "Horizontal Distance", "Horizontal Error", "ID", "Source", "Location Source", "Magnitude Source", "Status", "Depth", "Magnitude"]
#outputcols = ["Depth", "Magnitude"]
factors = data[["Latitude", "Longitude", "Timestamp"]]
results = data[["Depth", "Magnitude"]]
print(factors.shape)
print(results.shape)
X = factors.values
y = results.values
#y = y.astype(float)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)
#print(X_train.dtype)
#print(y_train.dtype)
#X_train = X_train.astype(float)
#print(np.unique(X_train))
#print(np.unique(y_train))

#Using KNN classifier
#n = 7
#KNN = KNeighborsClassifier(n_neighbors = n)
#KNN.fit(X_train, y_train)
#knn_yhat = KNN.predict(X_test)
#print('Accuracy score of the K-Nearest Neighbors model is {}'.format(accuracy_score(y_test, knn_yhat)))
#print('F1 score of the K-Nearest Neighbors model is {}'.format(f1_score(y_test, knn_yhat, average='weighted')))

#Using GaussionNB Neighbors classifier
#gnb = GaussianNB()
#gnb.fit(X_train, y_train)
#y_pred = gnb.predict(X_test)
#print('Accuracy score of the GaussianNB Neighbors model is {}'.format(accuracy_score(y_test, y_pred)))
#print("Gaussian Naive Bayes model accuracy(in %):", f1_score(y_test, y_pred, average='weighted')*100)

#Using Decision Tree Classifier
#dcs = DecisionTreeClassifier()
#dcs.fit(X_train, y_train)
#predictions = dcs.predict(X_test)
#print('Accuracy score of the Decision Tree Classifier model is {}'.format(accuracy_score(y_test, predictions)))
#print('F1 score of the Decision Tree Classifier model is {}'.format(f1_score(y_test, predictions, average='weighted')))

#Random Forest Classifier code below, but it takes a really long time to run and doesn't have the highest accuracy, so I've removed it from the code.
#rfc = RandomForestClassifier(n_estimators = 100)
#rfc.fit(X_train, y_train)
#predictions2 = rfc.predict(X_test)
#print('Accuracy score of the Random Tree Classifier model is {}'.format(accuracy_score(y_test, predictions2)))
#print('F1 score of the Random Tree Classifier model is {}'.format(f1_score(y_test, predictions2, average='weighted')))

#from sklearn.linear_model import LinearRegression
#lrg = LinearRegression()
#lrg.fit(X_train, y_train)
#lrgpred = lrg.predict(X_test)
#print(lrg.score(X_test, y_test))
#print(str(lrg.score(X_test, y_test)/lrg.score(X_test, lrgpred)))
#print(r2_score(y_test, lrgpred))

#from sklearn.linear_model import Ridge
#clf = Ridge(alpha=5.0)
#clf.fit(X_train, y_train)
#clfpred = clf.predict(X_test)
#print(clf.score(X_test, y_test))
#print(clf.score(X_test, clfpred))
#print(str(clf.score(X_test, y_test)/clf.score(X_test, clfpred)))

from sklearn.ensemble import RandomForestRegressor

reg = RandomForestRegressor(random_state=42)
reg.fit(X_train, y_train)
predictions2 = reg.predict(X_test)
print(X_test)
print(y_test)
print(predictions2)
print(reg.score(X_test, predictions2))
print(reg.score(X_test, y_test))
print(str(reg.score(X_test, y_test)/reg.score(X_test, predictions2)))
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Calculate mean squared error and root mean squared error
mse = mean_squared_error(y_test, predictions2)
rmse = mean_squared_error(y_test, predictions2, squared=False)

# Calculate mean absolute error
mae = mean_absolute_error(y_test, predictions2)

print("MSE: ", mse)
print("RMSE: ", rmse)
print("MAE: ", mae)
print(r2_score(y_test, predictions2))

#pickle.dump(reg, open('REGModel.pkl', 'wb'))
model = pickle.load(open('REGModel.pkl', 'rb'))
inputx = np.reshape(['37.72795665405347', '-122.35989905119452', '1678361421'], (1, -1))
print(model.predict(inputx))

#from sklearn import svm
#svmmod = svm.SVR()
#svmmod.fit(X_train, y_train)
#svmpred = svmmod.predict(X_test)
#print(svmmod.score(X_test, y_test))
#print(svmmod.score(X_test, svmpred))
#print(str(svmmod.score(X_test, y_test)/svmmod.score(X_test, svmpred)))
#print('Accuracy score of the Linear Regression model is {}'.format(accuracy_score(y_test, lrgpred)))
#print('F1 score of the Linear Regression model is {}'.format(f1_score(y_test, lrgpred, average='weighted')))