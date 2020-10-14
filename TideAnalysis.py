import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
Fill the blank values with 0.00-- not using
"""
def fillgaps(frames_to_use):
    frames_to_use.fillna(0.000)

"""
    Below code is to plot data
"""
def plot_row_data(data_sargent, data_nueces):
    fig, ax = plt.subplots()
    data_sargent.plot(x='#date+time', y='200-pwl', ax=ax, color='blue', label='Sargent Data')
    data_nueces.plot(x='#date+time', y='185-pwl', ax=ax, color='red', label='Nueces Data')
    plt.show()

"""
Rubric 1: plot_row_data, plot generic data
"""
if __name__ == '__main__':
    data_sargent_url = 'https://tamucc-ir.tdl.org/bitstream/handle/1969.6/87793/Sargent_RawDataOnly.csv?sequence=1&isAllowed=y'
    data_nueces_url = 'https://tamucc-ir.tdl.org/bitstream/handle/1969.6/87766/NuecesBay_RawDataOnly.csv?sequence=2&isAllowed=y'
    data_sargent = pd.read_csv(data_sargent_url)
    data_nueces = pd.read_csv(data_nueces_url)
    # plot_row_data(data_sargent, data_nueces) #plot generic data
    data_sargent.boxplot(by='#date+time', column=['200-pwl'], grid=False)


