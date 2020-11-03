import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
#from sklearn.metrics import r2_score, mean_squared_error
from math import sqrt

def sigmoid(x):
    return 1/(1+np.exp(-x))

def nn():
     # A 2 x 1 matrix of randomly generated weights in the range -1 to 1
    weights = np.random.uniform(-1, 1, size=(2, 1))
    print(weights)
    # The training set divided into input and output. Notice that
    # we are trying to train our neural network to predict the output
    # of the logical OR.
    training_inputs = np.array([[0, 0, 1, 1, 0, 1]]).reshape(3, 2)
    print(training_inputs)
    training_outputs = np.array([[0, 1, 1]]).reshape(3, 1)

    for i in range(15000):
        # forward pass
        dot_product = np.dot(training_inputs, weights)
        if i ==0:
            print(dot_product)
        output = sigmoid(dot_product)
        # backward pass.
        temp2 = -(training_outputs - output) * output * (1 - output)
        adj = np.dot(training_inputs.transpose(), temp2)
        # 0.5 is the learning rate.
        weights = weights - 0.5 * adj

    # The testing set
    test_input = np.array([1, 0])
    test_output = sigmoid(np.dot(test_input, weights))
    # OR of 1, 0 is 1
    print(test_output)

if __name__ == '__main__':
    nn()

# training = pd.read_csv('csv/BHPtraining_by_hour.csv',index_col=0)
# test = pd.read_csv('csv/BHPtest_by_hour.csv',index_col=0)

#print(training.head())
#training.plot()
#plt.show()
#model_arima = ARIMA(training,order=(5, 1, 5))
#model_arima_fit = model_arima.fit(disp=False)
#print(model_arima_fit.aic)

#period = 6
#predictions= model_arima_fit.forecast(steps=period)[0]
# actual = test[:period]
# plt.plot(actual)
# plt.plot(predictions,color='red')
# #plt.show()
# plt.savefig('png/result.png')
#
# print(actual)
# print(predictions)
#
# r2 = r2_score(actual, predictions)
# print('R^2:', r2)
#
# mse = mean_squared_error(actual, predictions)
# rmse = sqrt(mse)
# print('MSE', mse)
# print('RMSE:', rmse)
