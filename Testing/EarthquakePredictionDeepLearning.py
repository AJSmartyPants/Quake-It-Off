import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import math
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import datetime

# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return np.array(dataX), np.array(dataY)

# fix random seed for reproducibility
tf.random.set_seed(7)


# load the dataset
notimportantcols = ["Type", "Magnitude Type", "Magnitude Error", "Magnitude Seismic Stations", "Azimuthal Gap", "Horizontal Distance", "Horizontal Error", "ID", "Source", "Location Source", "Magnitude Source", "Status", "Depth Error", "Depth Seismic Stations", "Root Mean Square"]
data = read_csv("https://confrecordings.ams3.digitaloceanspaces.com/database.csv")
data = data[data["Type"].str.contains("Nuclear Explosion|Explosion|Rock Burst") == False]
data = data.drop(notimportantcols, axis = 1)

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
data = data.drop(["Date", "Time"], axis = 1)
#cols = ['Date', 'Time']
#data[cols] = data[cols].apply(le.fit_transform)
data['Magnitude'] = data['Magnitude'].astype(str).str.replace('.', '')
data['Depth'] = data['Depth'].astype(str).str.replace('.', '')
data = data[data != 'ValueError']
data.dropna(inplace=True)
dataset = data.values
dataset = dataset.astype('float32')

# normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 0.3))
dataset = scaler.fit_transform(dataset)

print(dataset)

# split into train and test sets
train_size = int(len(dataset) * 0.67)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]

print(train_size)
print(test_size)
print(train)
print(test)

# reshape into X=t and Y=t+1
look_back = 1
trainX, trainY = create_dataset(train, 1)
testX, testY = create_dataset(test, 1)


# reshape input to be [samples, time steps, features]
trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

print(trainX.shape)
print(testX.shape)
print(trainX)
print(testX)


# create and fit the LSTM network
model = Sequential()
model.add(LSTM(8, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=3, batch_size=1, verbose=2)
#epoch: number of times you train the model, improves accuracy, reduces loss, once loss stops reducing no need for more epochs
#batch_size: how much it runs in every epoch, batch_size cannot exceed epoch
#verbose: shows you the number of things
#loss: accuracy, minimal loss means the model is accurate
#train/test score: how much error is occuring in the prediction
#RMSE is root mean square error, calculation of error, used in regression

# make predictions
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

print(trainPredict)
print(testPredict)

# invert predictions
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform([testY])

# calculate root mean squared error
trainScore = np.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = np.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))

# shift train predictions for plotting
trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict

# shift test predictions for plotting
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

# plot baseline and predictions
plt.plot(dataset.inverse_transform(dataset))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()

#C:\Users\tinao\OneDrive\Desktop\Clevered MIT Internship ML\Not Disastrous\Testing\Airlines_passenger.csv