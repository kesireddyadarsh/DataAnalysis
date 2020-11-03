import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import signal
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
import tensorflow as tf

"""
Fill the blank values with 0.00-- not using
"""
def remove_high_fliers(frames_to_use,case_number):
    if case_number == 1:
        frames_to_use['data'] = frames_to_use['data'].where(frames_to_use['data'].between(9,11))
    elif case_number == 2:
        frames_to_use['tide'] = frames_to_use['tide'].where(frames_to_use['tide'].between(6, 9))

def sigmoid(x):
    return 1/(1+np.exp(-x))

if __name__ == '__main__':
    # A 2 x 1 matrix of randomly generated weights in the range -1 to 1
    weights = np.random.uniform(-1, 1, size=(2, 1))

    # The training set divided into input and output. Notice that
    # we are trying to train our neural network to predict the output
    # of the logical OR.
    training_inputs = np.array([[0, 0, 1, 1, 0, 1]]).reshape(3, 2)
    training_outputs = np.array([[0, 1, 1]]).reshape(3, 1)

    for i in range(15000):
        # forward pass
        dot_product = np.dot(training_inputs, weights)
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
    # data_nueces_url = 'https://tamucc-ir.tdl.org/bitstream/handle/1969.6/87766/NuecesBay_RawDataOnly.csv?sequence=2&isAllowed=y'
    # # download_url = '/Users/adarshkesireddy/Documents/Data/DataAnalysis/BHPtraining(1).csv'
    # download_url = '/Users/adarshkesireddy/Documents/Data/DataAnalysis/BHPtraining(1).csv'
    # data_nueces = pd.read_csv(data_nueces_url)
    # data = pd.read_csv(download_url)
    # data_nueces.rename(columns = {'#date+time': 'date_time', '185-pwl':'tide'}, inplace = True) #change the column names
    # """
    # Below code to clean tide data
    # """
    # remove_high_fliers(data_nueces, 2) #Removes high fliers
    # data_nueces = data_nueces.iloc[608880:] # remove first values
    # data_nueces = data_nueces.reset_index(drop=True) # reindex
    #
    # """
    # Below code to clean BHP training data and adjust tide data
    # """
    # data = data.drop(data.index[9040:38557])
    # data_nueces = data_nueces.drop(data.index[9040:38557])
    # data = data.reset_index(drop=True) # reindex
    # data_nueces = data_nueces.reset_index(drop=True) # reindex
    #
    # data = data.drop(data.index[52639:55626])
    # data_nueces = data_nueces.drop(data.index[52639:55626])
    # data = data.reset_index(drop=True) # reindex
    # data_nueces = data_nueces.reset_index(drop=True) # reindex
    #
    # data = data.drop(data.index[69060:83895])
    # data_nueces = data_nueces.drop(data.index[69060:83895])
    # data = data.reset_index(drop=True) # reindex
    # data_nueces = data_nueces.reset_index(drop=True) # reindex
    #
    # data = data.drop(data.index[82652:94473])
    # data_nueces = data_nueces.drop(data.index[82652:94473])
    # data = data.reset_index(drop=True) # reindex
    # data_nueces = data_nueces.reset_index(drop=True) # reindex
    #
    # data_nueces = data_nueces.iloc[1:] # remove first values
    # data = data.iloc[1:] # remove first values
    # data = data.reset_index(drop=True) # reindex
    # data_nueces = data_nueces.reset_index(drop=True) # reindex
    #
    # """
    # Interploation of the data
    # """
    # data_nueces["tide"] = data_nueces["tide"].interpolate()
    # data["Air Temperature"] = data["Air Temperature"].interpolate()
    # data["Water Level"] = data["Water Level"].interpolate()
    # data["Water Level Sigma"] = data["Water Level Sigma"].interpolate()
    # data["Wind Speed"] = data["Wind Speed"].interpolate()
    # data["Wind Direction"] = data["Wind Direction"].interpolate()
    # data["Wind Gust"] = data["Wind Gust"].interpolate()
    # # print(data)
    # # print(data_nueces)
    #
    # all_data = pd.concat([data_nueces, data], axis = 1)
    # all_data.drop('Date Time', axis=1, inplace=True)
    # all_data_numpy = all_data.to_numpy()
    # print(all_data)
    # print(all_data.keys())
    # print(all_data_numpy)

    # print(data.keys())
    # print(data[data['Air Temperature'].isnull()].index.tolist()) #print index of missing values
    # print(data)
    # numpy_tide = data_nueces.to_numpy()
    # numpy_rest = data.to_numpy()
    # all_date = np.append(numpy_tide[:,1],numpy_rest[:,1])
    # print(all_date)
    # print(data[data['Air Temperature'].isnull()].index.tolist()) #print index of missing values
    # data.info()
    # sns.heatmap(all_data.isnull(),cbar=False)
    # data_nueces.plot()
    # plt.xlabel("Tide level")
    # plt.ylabel("Time")
    # plt.title("New Data (Used for Prediction)")
    #print(data_nueces)
    #data_nueces.plot()
    # plt.show()
