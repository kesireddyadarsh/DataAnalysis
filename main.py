import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import signal
from scipy.optimize import curve_fit
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, median_absolute_error, max_error, explained_variance_score
from math import sqrt
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM



"""
Case_number -- 0 if imported data; 1 for noise data and imported data
"""
def plot_initial_value(case_number,path_x,path_y,noise_path_x):
    fig, ax = plt.subplots()
    ax.scatter(target_location_x,target_location_y,s=300,marker='o',c='green',label ='Target Location')
    ax.scatter(obstacle_location_x,obstacle_location_y,s=300,c='red',label = 'Obstacle Location')
    if case_number == 1:
        ax.plot(noise_path_x,path_y,c="skyblue", label ='Noise Path')
    ax.plot(path_x,path_y,c='navy',label = 'True Path')
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.legend(loc='lower left',markerscale=0.75)
    plt.show()


def plot_noise():
    plt.plot(noise, label="Noise")
    plt.xlabel('Time Step')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()


def plot_seasonal_acf():
    print("Temp")


def arima_model(training, testing):
    model_arima = ARIMA(training, order=(6, 0, 1))
    model_arima_fit = model_arima.fit(disp=False)
    predictions, semi, configuration = model_arima_fit.forecast(steps=len(testing))

    mse = round(mean_squared_error(testing, predictions), 3)
    rmse = round(sqrt(mse), 3)
    r2 = round(r2_score(testing, predictions), 3)
    mae = round(mean_absolute_error(testing, predictions), 3)
    med_abs_err = round(median_absolute_error(testing, predictions), 3)
    max_err = round(max_error(testing, predictions), 3)
    print(mse, rmse, r2, mae, med_abs_err, max_err)

    plt.plot(testing, label='actual')
    plt.plot(predictions, label='forecast')
    plt.legend(loc='lower left', markerscale=0.75)
    plt.xlabel("Time Step")
    plt.ylabel("Frequency")
    plt.show()

def lstm(training, testing):

    training_inputs = training
    training_inputs = training_inputs.reshape(len(training_inputs), 1, 1)
    training_outputs = np.append(training[1:], testing[0])

    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(1, 1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    print(model.summary())

    model.fit(training_inputs, training_outputs, epochs=20, validation_split=0.2, batch_size=5)

    test_input = testing
    test_input = test_input.reshape((len(testing), 1, 1))
    test_output = model.predict(test_input, verbose=0)
    test_input = testing
    test_output = test_output.reshape(len(testing))

    mse = round(mean_squared_error(test_input, test_output), 3)
    rmse = round(sqrt(mse), 3)
    r2 = round(r2_score(testing, test_output), 3)
    mae = round(mean_absolute_error(testing, test_output), 3)
    med_abs_err = round(median_absolute_error(testing, test_output), 3)
    max_err = round(max_error(testing, test_output), 3)
    print(mse, rmse, r2, mae, med_abs_err, max_err)

    plt.plot(test_input,label="Test Value")
    plt.plot(test_output,label="Prediction Value")
    plt.legend()
    plt.xlabel("Time Step")
    plt.ylabel("Frequency")
    plt.show()


"""
Path coordinates are of size 7519
Use 5000 data points for training
Reward 4500 
"""
if __name__ == '__main__':
    print_noise = False #True to print only noise
    arima_case_1 = False #for case 1 using arima
    arima_case_2 = True #for case 2 using arima
    lstm_case_1 = False #for case 1 using lstm
    lstm_case_2 = False #for case 2 using lstm

    #url = "/home/ak/Documents/DataAnalysis/Project/data.csv"
    # url_1 = "/home/ak/Documents/DataAnalysis/Project/data_1.csv"

    url = "/Users/adarshkesireddy/Downloads/DataAnalysis-main/data.csv"
    url_1 = "/Users/adarshkesireddy/Downloads/DataAnalysis-main/data_1.csv"

    data_training_1 = pd.read_csv(url)
    data_x_training_1 = data_training_1.loc[:,'x']
    data_y_training_1 = data_training_1.loc[:,'y']
    path_x_training_1 = data_x_training_1.values
    path_y_training_1 = data_y_training_1.values

    data_training_2 = pd.read_csv(url_1)
    data_x_training_2 = data_training_2.loc[:,'x']
    data_y_training_2 = data_training_2.loc[:,'y']
    path_x_training_2 = data_x_training_2.values
    path_y_training_2 = data_y_training_2.values


    target_location_x = np.array([5, 40, 95, 95, 95])
    target_location_y = np.array([95, 95, 95, 40, 5])
    obstacle_location_x = np.array([22, 60, 95, 95, 50, 5, 60, 20, 75, 30])
    obstacle_location_y = np.array([95, 95, 60, 22, 50, 25, 5, 65, 65, 30])
    #plot_initial_value()

    noise = np.random.uniform(-5,5,len(path_x_training_1))
    noise_1 = np.random.uniform(-5,5,len(path_x_training_1))

    # noise = np.random.normal(size=(len(path_x_training_1)))
    # noise_1 = np.random.normal(size=(len(path_x_training_2)))

    if print_noise:
        plot_noise()


    #
    if len(noise) < len(path_x_training_1):
        noise_path_x_training_1 = path_x_training_1.copy()
        noise_path_x_training_1[:len(noise)] += noise
    else:
        noise_path_x_training_1 = noise.copy()
        noise_path_x_training_1[:len(path_x_training_1)] += path_x_training_1

    if len(noise_1) < len(path_x_training_2):
        noise_path_x_training_2 = path_x_training_2.copy()
        noise_path_x_training_2[:len(noise_1)] += noise_1
    else:
        noise_path_x_training_2 = noise_1.copy()
        noise_path_x_training_2[:len(path_x_training_2)] += path_x_training_2


    # plot_initial_value(1,path_x_training_1,path_y_training_1,noise_path_x_training_1)
    # plot_initial_value(1,path_x_training_2,path_y_training_2,noise_path_x_training_2)

    #divide the data
    training_value_1 = noise_path_x_training_1[:6000]
    test_value_1 = noise_path_x_training_1[6000:]

    training_value_2 = noise_path_x_training_2[:6000]
    test_value_2 = noise_path_x_training_2[6000:]
    print(len(training_value_2),len(test_value_2))
    if arima_case_1:
        arima_model(training_value_1,test_value_1)
    if arima_case_2:
        arima_model(training_value_2,test_value_2)

    if lstm_case_1:
        lstm(training_value_1,test_value_1)
    if lstm_case_2:
        lstm(training_value_2,test_value_2)
    #
    # arima_model()
    # X = data_x_test.values
    # size = int(len(X) * 0.66)
    # train, test = X[0:size], X[size:len(X)]
    # print(train,test)
    # history = [x for x in train]
    # print(history)

    # plt.plot(noise_path_x_training)
    # plt.plot(path_x_training)
    # plt.xlabel("Time Step")
    # plt.ylabel("Frequency")
    # plt.title("Noise vs Actual Data")
    # plt.show()


