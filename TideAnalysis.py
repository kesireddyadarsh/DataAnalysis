import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""
Fill the blank values with 0.00-- not using
"""
def fillgaps(frames_to_use):
    # print(frames_to_use)
    # frames_to_use.fillna(0.000)
    # frames_to_use.stack().apply(pd.to_numeric, errors='ignore').fillna(0).unstack()
    frames_to_use['data']=frames_to_use['data'].where(frames_to_use['data'].between(6,12))

    # frames_to_use['200-pwl'] = frames_to_use['200-pwl'].replace(np.nan, 0) #working
    # frames_to_use.to_csv(r'/home/ak/Documents/DataAnalysis/DataAnalysis/File_Name.csv', index = False)


"""
    Below code is to plot data
"""
# def plot_row_data_sargent(data_sargent):
#     data_sargent.plot(x='#date+time', y='200-pwl', color='blue', label='Sargent Data')
#     plt.show()
#
# def plot_row_data_nueces(data_nueces):
#     data_nueces.plot(x='#date+time', y='185-pwl',  color='red', label='Nueces Data')
#     plt.show()

def plot_row_data(data_sargent,data_nueces):
    fig, ax = plt.subplots()
    data_sargent.plot(x='#date+time', y='data', ax = ax, color='blue', label='Sargent Data')
    data_nueces.plot(x='#date+time', y='data', ax = ax, color='red', label='Nueces Data')
    plt.show()

"""
Rubric 1: plot_row_data, plot generic data
"""
if __name__ == '__main__':
    data_sargent_url = 'https://tamucc-ir.tdl.org/bitstream/handle/1969.6/87793/Sargent_RawDataOnly.csv?sequence=1&isAllowed=y'
    data_nueces_url = 'https://tamucc-ir.tdl.org/bitstream/handle/1969.6/87766/NuecesBay_RawDataOnly.csv?sequence=2&isAllowed=y'
    data_sargent = pd.read_csv(data_sargent_url)
    data_nueces = pd.read_csv(data_nueces_url)
    data_sargent.rename(columns = {'200-pwl':'data'}, inplace = True)
    data_nueces.rename(columns = {'185-pwl':'data'}, inplace = True)
    """
    Uncomment below code to open raw data
    """
    # plot_row_data_sargent(data_sargent) #plot generic data
    # plot_row_data_nueces(data_nueces) #plot generic data
    plot_row_data(data_sargent,data_nueces)
    """
    Cleaning the data:
        1. Remove outliners
        2. Find the mean of given time and place it
    """
    # print(data_nueces.loc[67]) #to access location
    # fillgaps(data_sargent)
    # fillgaps(data_nueces)
    # plot_row_data_sargent(data_sargent)
    # plot_row_data_sargent(data_nueces)
    # data_sargent.boxplot(by='#date+time', column=['200-pwl'], grid=False)
    # sns.boxenplot(x=data_sargent['#date+time'], y=data_sargent['200-pwl'])
    # plt.boxplot(x=data_sargent['200-pwl'])
    # plt.show()


