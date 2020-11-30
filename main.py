import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import signal

def plot_initial_value():
    plt.scatter(target_location_x,target_location_y,s=500,marker='o',c='green')
    plt.scatter(obstacle_location_x,obstacle_location_y,s=300,c='red')
    plt.plot(path_x,path_y,)
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.show()

"""
Path coordinates are of size 7519
Use 5000 data points for training
"""
if __name__ == '__main__':
    # print("This is working")
    url = "/home/ak/Documents/DataAnalysis/Project/data.csv"
    data = pd.read_csv(url)
    data_x = data.loc[:,'x']
    data_y = data.loc[:,'y']
    path_x = data_x.values
    path_y = data_y.values
    target_location_x = np.array([5, 40, 95, 95, 95])
    target_location_y = np.array([95, 95, 95, 40, 5])
    obstacle_location_x = np.array([22, 60, 95, 95, 50, 5, 60, 20, 75, 30])
    obstacle_location_y = np.array([95, 95, 60, 22, 50, 25, 5, 65, 65, 30])
    #plot_initial_value()



