#Decision Tree Classifier
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

dcs = DecisionTreeClassifier()
data = pd.read_csv("https://confrecordings.ams3.digitaloceanspaces.com/CreditCard_9820.csv")
data.dropna(inplace = True)
fraud = data[data['Class'] == 1]
valid = data[data['Class'] == 0]
outlierFraction = len(fraud)/float(len(valid))
print(outlierFraction) #outlier is the noise in the data (random/dummy values)
print('Fraud Cases: {}'.format(len(data[data['Class'] == 1])))
print('Valid Transactions: {}'.format(len(data[data['Class'] == 0])))
X = data.drop(['Class'], axis = 1)
Y = data['Class']
print(X.shape)
print(Y.shape)
X = X.values
y = Y.values
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)

dcs.fit(X_train, y_train)
predictions = dcs.predict(X_test)
print('Accuracy score of the Decision Tree Classifier model is {}'.format(accuracy_score(y_test, predictions)))
print('F1 score of the Decision Tree Classifier model is {}'.format(f1_score(y_test, predictions)))

#Random Tree Classifier
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators = 100)
rfc.fit(X_train, y_train)
predictions2 = rfc.predict(X_test)
print('Accuracy score of the Random Tree Classifier model is {}'.format(accuracy_score(y_test, predictions2)))
print('F1 score of the Random Tree Classifier model is {}'.format(f1_score(y_test, predictions2)))

#Out of a few test runs, the Random Tree Classifier seems to have a higher accuracy.