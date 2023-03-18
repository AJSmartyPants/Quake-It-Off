import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import datetime
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, r2_score
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.datasets import load_diabetes
import time
#import datetime

#Setting the data, removing null values
data = pd.read_csv("https://confrecordings.ams3.digitaloceanspaces.com/silver.csv")
data = data[['date', 'hour', 'latitude', 'longitude', 'depth', 'mag']]
data = data[:50000]
data.dropna(inplace=True) 
datetime_str = data["date"] + " " + data["hour"].astype(str) + ":00:00"

# Convert the concatenated string to a datetime object
datetime_obj = pd.to_datetime(datetime_str, format="%Y-%m-%d %H:%M:%S")

# Add the datetime column to the dataframe
data["datetime"] = datetime_obj
data["timestamp"] = data["datetime"].apply(datetime.datetime.timestamp)

# Drop the original "date" and "hour" columns
data = data.drop(["date", "hour", "datetime"], axis=1)

# Save the updated dataframe to a new CSV file
#data = data.to_csv("silver_with_datetime.csv", index=False)
print(data.columns)
print(data.shape)
print(data.head(3)) 

factors = data[["timestamp", "latitude", "longitude"]]
results = data[["depth", "mag"]]
print(factors.shape)
print(results.shape)
X = factors.values
y = results.values
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)

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

pickle.dump(reg, open('EQPModel.pkl', 'wb'))
model = pickle.load(open('EQPModel.pkl', 'rb'))
inputx = np.reshape(['1686424879', '37.369', '-117.714'], (1, -1))
print(model.predict(inputx))