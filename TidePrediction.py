import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import signal
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
from keras.models import Sequential
from keras.layers import Dense
from keras import backend as K
from sklearn.metrics import r2_score

#https://machinelearningmastery.com/how-to-choose-loss-functions-when-training-deep-learning-neural-networks/

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

def nn():
    weights = np.random.uniform(-1, 1, size=(6, 1))
    # weights = np.random.uniform(-1, 1, size=(2, 1))
    # training_inputs = np.array([[0, 0, 1, 1, 0, 1]]).reshape(3, 2)
    # training_outputs = np.array([[0, 1, 1]]).reshape(3, 1)

    transpose_new_list = np.array(new_list).transpose()
    minmax = []
    for i in range(0,6):
        max_value = max(transpose_new_list[i])
        min_value = min(transpose_new_list[i])
        minmax.append([min_value, max_value])

    # pprint(minmax)
    for i in range(0,len(new_list)):
        for j in range(0,6):
            new_list[i][j] = ((new_list[i][j] - minmax[j][0])/(minmax[j][1] - minmax[j][0]))
    training_inputs = new_list
    training_inputs.pop()
    print(len(training_inputs))
    # pprint(new_list[:10])
    # print(len(new_list))
    # print(training_inputs)

    temp_storage = transpose_new_list[1][1:]
    for i in range(0,len(temp_storage)):
        temp_storage[i] = ((temp_storage[i] - minmax[1][0])/(minmax[1][1] - minmax[1][0]))
    training_outputs = temp_storage
    print(len(training_outputs))

    combined_list = []
    for i,o in zip(training_inputs, training_outputs):
        temp = [*i, o]
        combined_list.append(temp)

    training_inputs = np.asarray(training_inputs).astype('float32')
    training_outputs = np.asarray(training_outputs).astype('float32')
    model = Sequential()
    model.add(Dense(12, input_dim=6, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # model.fit(training_inputs, training_outputs, epochs=150, batch_size=10)
    # model.fit(training_inputs, training_outputs, epochs=150, batch_size=10)
    # _, accuracy = model.evaluate(training_inputs, training_outputs)
    # print('Accuracy: %.2f' % (accuracy*100))

    history = model.fit(training_inputs, training_outputs, validation_data=(training_inputs, training_outputs), epochs=100, verbose=0)
    # evaluate the model
    train_mse = model.evaluate(training_inputs, training_outputs, verbose=0)
    test_mse = model.evaluate(training_inputs, training_outputs, verbose=0)
    print(train_mse, test_mse)
    #print('Train: %.3f, Test: %.3f' % (train_mse, test_mse))

    """
    Below to find r^2
    """
    r2 = r2_score(history.history['val_loss'], history.history['loss'])
    print(r2)
    print(history.history['val_loss'][:12])
    print(history.history['loss'][:12])
    """
    Below code to find mean squared error
    """
    # # plot loss during training
    # plt.title('Loss / Mean Squared Error')
    # plt.plot(history.history['loss'], label='train')
    # plt.plot(history.history['val_loss'], label='test')
    # plt.legend()
    # plt.show()

    """
    Below code for neural network
    """
    # print(combined_list[:3])
    # data_set = [training_inputs, training_outputs]
    # pprint(data_set[:2])
    # for i in 1:
    #     # forward pass
    #     dot_product = np.dot(training_inputs, weights)
    #     dot_product = dot_product.astype(np.float128)
    #     # if i ==0:
    #     #     print(dot_product)
    #     output = sigmoid(dot_product)
    #
    #     # backward pass.
    #     temp2 = -(training_outputs - output) * output * (1 - output)
    #     adj = np.dot(transpose_new_list, temp2)
    #     # 0.5 is the learning rate.
    #     weights = weights - 0.5 * adj

    # The testing set
    # test_input = np.array([1, 0])
    # test_output = sigmoid(np.dot(test_input, weights))
    #

    """
    Below code for prediction
    """
    test_input = new_list_test[:6]
    test_input = np.asarray(test_input).astype('float32')
    predictions = model.predict(test_input)
    print(predictions)
    # round predictions
    rounded = [round(x[0]) for x in predictions]
    print(rounded)
    # test_output = sigmoid(np.dot(test_input, weights))
    # # OR of 1, 0 is 1
    # print(test_output)

if __name__ == '__main__':
   data_nueces_url = 'https://tamucc-ir.tdl.org/bitstream/handle/1969.6/87766/NuecesBay_RawDataOnly.csv?sequence=2&isAllowed=y'
   # download_url = '/Users/adarshkesireddy/Documents/Data/DataAnalysis/BHPtraining(1).csv' #personal
   download_url = '/home/ak/Documents/DataAnalysis/DataAnalysis/DataAnalysis/BHPtraining.csv' #work
   download_url_test = '/home/ak/Documents/DataAnalysis/DataAnalysis/DataAnalysis/BHPtest.csv' #work
   data_nueces = pd.read_csv(data_nueces_url)
   data = pd.read_csv(download_url)
   data_test = pd.read_csv(download_url_test)
   data_nueces.rename(columns = {'#date+time': 'date_time', '185-pwl':'tide'}, inplace = True) #change the column names
   """
   Below code to clean tide data
   """
   remove_high_fliers(data_nueces, 2) #Removes high fliers
   data_nueces = data_nueces.iloc[608880:] # remove first values
   data_nueces = data_nueces.reset_index(drop=True) # reindex

   """
   Below code to clean BHP training data and adjust tide data
   """
   data = data.drop(data.index[9040:38557])
   data_nueces = data_nueces.drop(data.index[9040:38557])
   data = data.reset_index(drop=True) # reindex
   data_nueces = data_nueces.reset_index(drop=True) # reindex

   data = data.drop(data.index[52639:55626])
   data_nueces = data_nueces.drop(data.index[52639:55626])
   data = data.reset_index(drop=True) # reindex
   data_nueces = data_nueces.reset_index(drop=True) # reindex
   data = data.drop(data.index[69060:83895])
   data_nueces = data_nueces.drop(data.index[69060:83895])
   data = data.reset_index(drop=True) # reindex
   data_nueces = data_nueces.reset_index(drop=True) # reindex

   data = data.drop(data.index[82652:94473])
   data_nueces = data_nueces.drop(data.index[82652:94473])
   data = data.reset_index(drop=True) # reindex
   data_nueces = data_nueces.reset_index(drop=True) # reindex

   data_nueces = data_nueces.iloc[1:] # remove first values
   data = data.iloc[1:] # remove first values
   data = data.reset_index(drop=True) # reindex
   data_nueces = data_nueces.reset_index(drop=True) # reindex

   """
   Interploation of the data
   """
   data_nueces["tide"] = data_nueces["tide"].interpolate()
   data["Air Temperature"] = data["Air Temperature"].interpolate()
   data["Water Level"] = data["Water Level"].interpolate()
   data["Water Level Sigma"] = data["Water Level Sigma"].interpolate()
   data["Wind Speed"] = data["Wind Speed"].interpolate()
   data["Wind Direction"] = data["Wind Direction"].interpolate()
   data["Wind Gust"] = data["Wind Gust"].interpolate()

   # print(data)
   data_numpy = data.to_numpy()
   data_test_numpy = data_test.to_numpy()

   """
   Test data
   """
   new_list_test = []
   for i, row in enumerate(data_test_numpy):
       if row[0][11:13] in ["00", "12"] and row[0][14:16] == "06":
           new_list_test.append(row[1:])

   """
   Training data
   """
   new_list = []
   for i, row in enumerate(data_numpy):
       if row[0][11:13] in ["00", "12"] and row[0][14:16] == "06":
           new_list.append(row[1:])

   """
   Model and prediction
   """
   nn()

   # pprint(new_list[:5])
    # test_input = new_list_test[:6]
   # print(len(test_input))
   # print(data_numpy[0][0][14:16])
   # print(data_numpy[1][0][14:16])
   # print(data_numpy[2][0][11:16])
   #print(new_list)
   # print(data)
   # print(data_nueces)

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
