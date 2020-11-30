import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import signal


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
    plt.legend(loc='upper right',markerscale=0.75)
    plt.show()

"""
Path coordinates are of size 7519
Use 5000 data points for training
Reward 4500 
"""
if __name__ == '__main__':
    # print("This is working")
    url = "/home/ak/Documents/DataAnalysis/Project/data.csv"
    url_1 = "/home/ak/Documents/DataAnalysis/Project/data_1.csv"

    data_training = pd.read_csv(url)
    data_x_training = data_training.loc[:,'x']
    data_y_training = data_training.loc[:,'y']
    path_x_training = data_x_training.values
    path_y_training = data_y_training.values

    data_test = pd.read_csv(url_1)
    data_x_test = data_test.loc[:,'x']
    data_y_test = data_test.loc[:,'y']
    path_x_test = data_x_test.values
    path_y_test = data_y_test.values

    target_location_x = np.array([5, 40, 95, 95, 95])
    target_location_y = np.array([95, 95, 95, 40, 5])
    obstacle_location_x = np.array([22, 60, 95, 95, 50, 5, 60, 20, 75, 30])
    obstacle_location_y = np.array([95, 95, 60, 22, 50, 25, 5, 65, 65, 30])
    #plot_initial_value()

    # noise = np.random.uniform(-1,1,len(path_x_training))
    noise = np.random.normal(size=(len(path_x_training)))
    print(len(noise),noise)
    plt.plot(noise)
    plt.show()
    if len(noise) < len(path_x_training):
        noise_path_x_training = path_x_training.copy()
        noise_path_x_training[:len(noise)] += noise
    else:
        noise_path_x_training = noise.copy()
        noise_path_x_training[:len(path_x_training)] += path_x_training

    if len(noise) < len(path_x_test):
        noise_path_x_test = path_x_test.copy()
        noise_path_x_test[:len(noise)] += noise
    else:
        noise_path_x_test = noise.copy()
        noise_path_x_test[:len(path_x_test)] += path_x_test

    if len(noise_path_x_test) != len(path_y_test):
        path_y_test = np.delete(path_y_test,len(noise_path_x_test)-1)


    # plot_initial_value(1,path_x_training,path_y_training,noise_path_x_training)
    plot_initial_value(1,path_x_test,path_y_test,noise_path_x_test)

