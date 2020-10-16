import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import signal
import datetime as dt

def plot_row_data(data):
    fig, ax = plt.subplots(nrows=2, ncols=2)
    data.plot(y='x', ax= ax[0,0], color='blue')
    data.plot(y='y', ax= ax[0,1], color='red')
    data.plot(y='z', ax= ax[1,0], color='black')
    data.plot(y='w', ax= ax[1,1], color='black')
    # plt.xlabel('Time series')
    # plt.ylabel('Value/frequency')
    plt.show()

def boxplot_values(data):
    plt.boxplot(data)
    plt.show()

def autocorrelate_plots(data):
    fig, ax = plt.subplots(nrows=2, ncols=2)
    pd.plotting.autocorrelation_plot(data['x'], ax=ax[0, 0])
    pd.plotting.autocorrelation_plot(data['y'], ax=ax[0, 1])
    pd.plotting.autocorrelation_plot(data['z'], ax=ax[1, 0])
    pd.plotting.autocorrelation_plot(data['w'], ax=ax[1, 1])
    # data.plot(y='x', ax=ax[0, 0], color='blue')
    # data.plot(y='y', ax=ax[0, 1], color='red')
    # data.plot(y='z', ax=ax[1, 0], color='black')
    # data.plot(y='w', ax=ax[1, 1], color='black')
    # plt.xlabel('Time series')
    # plt.ylabel('Value/frequency')
    plt.show()

if __name__ == '__main__':
    data_url = '/Users/adarshkesireddy/Downloads/data.csv'
    data = pd.read_csv(data_url)
    """
    Below line to plot raw data
    """
    # plot_row_data(data)
    # print(data.keys())
    # print(data[data['y'].isnull()].index.tolist())
    # print(data['x'].Period())
    # print(data['y'].isnull())
    """
        Below line to  box plot data
    """
    # boxplot_values(data)
    """
    Below line to interpolate
    """
    data['y'] = data['y'].interpolate()
    """
            Below line to  box plot data
    """
    # boxplot_values(data)

    """
    Below plot are for correlation 
    """
    # autocorrelate_plots(data)

    """
    Below two lines are code for correlation
    """
    # print(data.corr(method='pearson'))
    # print(data.corr(method='spearman'))

    """
        Scatter plot and histogram
    """
    # sns.pairplot(data)
    # plt.show()


    # mean_x = pd.Series(data['x']).rolling(window=2).mean()
    # itr = range(len(mean_x))
    # plt.plot(itr, mean_x)
    # data.diff().plot(figsize=(20, 10), linewidth=5, fontsize=20)
    # idx = pd.date_range('2018-01-01', periods=len(data), freq='H')
    # data.insert(0, 'Timestamp', idx)
    #

    # print(data)
    # plt.show()
    # pd.plotting.autocorrelation_plot(data['y'])
    # pd.plotting.autocorrelation_plot(data['z'])
    # pd.plotting.autocorrelation_plot(data['w'])
    # plt.show()
    # sns.pairplot(data)
    # fig, ax = plt.subplots()
    # ax.boxplot(data.values())
    # ax.set_xticklabels(data.keys())
    # plt.show()

    # print(data['x'].autocorr())