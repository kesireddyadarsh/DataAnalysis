import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import signal
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm

"""
Fill the blank values with 0.00-- not using
"""
def remove_high_fliers(frames_to_use,case_number):
    if case_number == 1:
        frames_to_use['data'] = frames_to_use['data'].where(frames_to_use['data'].between(9,11))
    elif case_number == 2:
        frames_to_use['data'] = frames_to_use['data'].where(frames_to_use['data'].between(6, 9))
    # print(frames_to_use)
    # frames_to_use.fillna(0.000)
    # frames_to_use.stack().apply(pd.to_numeric, errors='ignore').fillna(0).unstack()
    # frequency = 240
    # while frequency < len(frames_to_use):
    #     working_frame = frames_to_use.head(frequency)
    #     list_of_names = working_frame['data'].to_list()
    #     for i in range(0, len(list_of_names)):
    #         print(i)
    #     frequency += 240
    #
    #
    # # for frequency  in :
    # #     print(i, j)
    # #     frames_to_use['date_time'].replace({i: i.replace('T', ' ')})
    # #     print(frames_to_use['date_time'][0])
    # frames_to_use['200-pwl'] = frames_to_use['200-pwl'].replace(np.nan, 0) #working
    # frames_to_use.to_csv(r'/home/ak/Documents/DataAnalysis/DataAnalysis/File_Name.csv', index = False)

def nueces_remove_data(data_nueces):
    print("just check")

"""
    Below code is to plot data
"""
def plot_row_data_sargent(data_sargent):
    data_sargent.plot(x='date_time', y='data', color='blue', label='Sargent Data')
    plt.show()
#
# def plot_row_data_nueces(data_nueces):
#     data_nueces.plot(x='#date+time', y='185-pwl',  color='red', label='Nueces Data')
#     plt.show()

def plot_row_data(data_sargent,data_nueces):
    fig, ax = plt.subplots()
    data_sargent.plot(x='date_time', y='data', ax = ax, color='blue', label='Sargent Data')
    data_nueces.plot(x='date_time', y='data', ax = ax, color='red', label='Nueces Data')
    plt.suptitle("Raw Data Plot")
    plt.show()

def box_plot_fill_data(frames_to_use):
    # data_sargent["data"] = data_sargent["data"].rolling(window = 5).mean
    frames_to_use["data"] = frames_to_use["data"].interpolate()
    frames_to_use['day'] = frames_to_use['date_time'].apply(lambda x: x.date())
    frames_to_use['year'] = frames_to_use['date_time'].apply(lambda x: x.year)
    frames_to_use['month'] = frames_to_use['date_time'].apply(lambda x: x.month)
    frames_to_use['time_of_day'] = frames_to_use['date_time'].apply(lambda x: x.time())
    # data_nueces["data"] = data_nueces["data"].rolling(window = 5).mean
    # plot_row_data(data_sargent, data_nueces)
    # fig, ax = plt.subplots()
    # frames_to_use.boxplot(by='year', column=['data'], grid=False)
    # data_nueces.plot(x='date_time', y='data', ax=ax, color='red', label='Nueces Data')
    # plt.show()
    # plt.show()

def plot_box(frames,value,label_name):
    frames.boxplot(by=value, column=['data'], grid=False)
    plt.suptitle(label_name)
    plt.show()

def histogram_intersection(a, b):
    v = np.minimum(a, b).sum().round(decimals=1)
    return v


if __name__ == '__main__':
    data_sargent_url = 'https://tamucc-ir.tdl.org/bitstream/handle/1969.6/87793/Sargent_RawDataOnly.csv?sequence=1&isAllowed=y'
    data_nueces_url = 'https://tamucc-ir.tdl.org/bitstream/handle/1969.6/87766/NuecesBay_RawDataOnly.csv?sequence=2&isAllowed=y'
    data_sargent = pd.read_csv(data_sargent_url)
    data_nueces = pd.read_csv(data_nueces_url)
    data_sargent.rename(columns = {'#date+time': 'date_time', '200-pwl':'data'}, inplace = True)
    data_nueces.rename(columns = {'#date+time': 'date_time', '185-pwl':'data'}, inplace = True)
    temp_date_sargent = pd.date_range('2012-11-09', periods=len(data_sargent), freq='6min')
    temp_date_nueces = pd.date_range('2010-01-21', periods=len(data_nueces), freq='6min')
    data_sargent = data_sargent.assign(date_time=temp_date_sargent)
    data_nueces = data_nueces.assign(date_time=temp_date_nueces)
    # print(data_sargent)
    # print(data_nueces)
    # data_sargent.replace(data_sargent[:, 0], i[:, 0])
    """
    Uncomment below code to plot raw data
    """
    # plot_row_data(data_sargent, data_nueces)
    """
    Cleaning the data:
        1. Remove outliners
        2. Find the mean of given time and place it
    """
    remove_high_fliers(data_sargent, 1)
    remove_high_fliers(data_nueces, 2)
    """
    Uncomment this code to obtain boxplots
    """
    box_plot_fill_data(data_sargent)
    box_plot_fill_data(data_nueces)
    data_sargent = data_sargent.dropna()
    data_sargent = data_sargent.reset_index(drop = True)
    data_nueces = data_nueces.dropna()
    data_nueces = data_nueces.reset_index(drop = True)
    # print(data_nueces)
    """
    Below code to perform box plot
    """
    # plot_box(data_sargent,'month', 'Data Sargent per month')
    """
    Below code is for auto correlation and partial correlation
    """
    # plot_acf(data_nueces['data'])
    # # plot_pacf(data_nueces['data'])
    # plt.suptitle('Nueces Data')
    # plt.show()
    # print(data_nueces.corr())
    # print(data_sargent.corr())

    """
    This is for periodogram
    """
    # f, Pxx_den = signal.periodogram(data_sargent['data'])
    # plt.semilogy(f, Pxx_den)
    # plt.suptitle('Sargent Data')
    # plt.show()
    """
    This is for season
    """
    # print(data_sargent)
    # data_sargent['date_time'] = pd.to_datetime(data_sargent['date_time'])
    # data_sargent = data_sargent.set_index('date_time')
    # season_plt = sm.tsa.seasonal_decompose(data_sargent, model='additive', period=365)
    # season_plt.plot()
    # plt.show()
    season_plt = seasonal_decompose(data_nueces['data'], model='additive', period=365)
    season_plt.plot()
    plt.show()
    # pd.plotting.autocorrelation_plot(data_sargent['data'])
    # print(data_nueces.loc[67]) #to access location
    # fillgaps(data_sargent)
    # fillgaps(data_nueces)



    # plot_row_data_sargent(data_sargent)
    # plot_row_data_sargent(data_nueces)
    # data_sargent.boxplot(by='#date+time', column=['200-pwl'], grid=False)
    # sns.boxenplot(x=data_sargent['#date+time'], y=data_sargent['200-pwl'])
    # plt.boxplot(x=data_sargent['200-pwl'])
    # plt.show()


    # data_sargent.drop(data_sargent[data_sargent.isnull().sum(axis=1)>5].index,axis=0,inplace=True)
    # d = np.where(data_sargent.isnull().sum(axis=1) >= 1)
    # data_sargent = data_sargent.drop(data_sargent.index[d])
    # data_nueces = data_nueces.iloc[245520:]
    # data_nueces = data_nueces.drop(data_nueces.index[d])


    # # data_sargent["data"] = data_sargent["data"].rolling(window = 5).mean

    # # data_nueces["data"] = data_nueces["data"].rolling(window = 5).mean
    # # plot_row_data(data_sargent, data_nueces)
    #
    # data_sargent['day'] = data_sargent['date_time'].apply(lambda x: x.date())
    # data_sargent['year'] = data_sargent['date_time'].apply(lambda x: x.year)
    # data_sargent['month'] = data_sargent['date_time'].apply(lambda x: x.month)
    # data_sargent['time_of_day'] = data_sargent['date_time'].apply(lambda x: x.time())
    # # print(data_sargent)
    #
    # plt.show()
    # data_sargent.boxplot()
    # plt.show()

    # data_sargent.boxplot(by='year', column=['data'], grid=False)
    # data_sargent.boxplot(by='month', column=['data'], grid=False)
    # data_nueces.boxplot(by='year', column=['data'], grid=False)
    # data_nueces.boxplot(by='month', column=['data'], grid=False)
    # plt.show()

    """
    Auto and partial correlation
    """
    # print(data_nueces.corr())
    # print(data_sargent)
    # print(data_sargent.corrwith(data_sargent['data'], method='pearson'))

    """
    This is for graphs
    """
    # data_7d_rol = data_sargent['data'].rolling(window=7, center=True).mean()
    # data_365d_rol = data_sargent['data'].rolling(window=365, center=True).mean()
    #
    # fig, ax = plt.subplots(figsize=(11, 4))  # plotting daily data
    # ax.plot(data_sargent['data'], marker='.', markersize=2, color='0.6', linestyle='None', label='Daily')  # plotting 7-day rolling data
    # ax.plot(data_7d_rol, linewidth=2, label='7-d Rolling Mean')# plotting annual rolling data
    # ax.plot(data_365d_rol, color='0.2', linewidth=3, label='Trend (365-d Rolling Mean)')  # Beautification of plot
    # # ax.xaxis.set_major_locator(mdates.YearLocator())
    # # ax.legend()
    # # ax.set_xlabel('Year')
    # # ax.set_ylabel('Consumption (GWh)')
    # # ax.set_title('Trends in Electricity Consumption')
    # plt.show()

    # data_sargent['Unit'] = data_sargent.groupby(['data', 'month']).cumcount()
    # ax = sns.tsplot(time='month', value="Overload", ci=100, unit="Unit", data=data_sargent)

    # grouped = data_sargent.groupby(["data", "month"]).agg({'Overload': ['min', 'mean', 'max']}).unstack("data")
    # axes = grouped.loc[:, ('Overload', 'mean')].plot(subplots=True)
    # palette = sns.color_palette()
    # index = 0
    # for ax in axes:
    #     ax.fill_between(grouped.index, grouped.loc[:, ('Overload', 'mean', index + 1)],
    #                     grouped.loc[:, ('Overload', 'max', index + 1)], alpha=.2, color=palette[index])
    #     ax.fill_between(grouped.index,
    #                     grouped.loc[:, ('Overload', 'min', index + 1)], grouped.loc[:, ('Overload', 'mean', index + 1)],
    #                     alpha=.2, color=palette[index])
    #     index += 1
    # data_1.reset_index(inplace=True)
    # fig, ax = plt.subplots()
    # ax = data_1.plot(x='year', y='Mean', c='white')
    # plt.fill_between(x='year', y1='Low Value', y2='High Value', data=data_1)
    # plt.show()

    # numpy_sargent = data_sargent.to_numpy()
    # numpy_nueces = data_nueces.to_numpy()
    # print(numpy_nueces[68])
    # data_sargent.to_csv(r'/home/ak/Documents/DataAnalysis/DataAnalysis/File_Name.csv', index = False)
    # plot_acf(data_sargent['data'])
    # plt.show()

