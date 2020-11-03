import numpy as np
import csv
import os
import datetime
import statistics
import matplotlib.pyplot as plt
from scipy import stats

# pandas & statsmodels importing
import pandas as pd
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
register_matplotlib_converters()

def data_resampling(target_file, downsample_factor):
    ori_list = []
    filling_cnt = 0
    with open(target_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        is_date_ok = False
        for row in reader:
            dt, temp, wl, wls, ws, wd, wg  = row
            #dt, pwl = dt.strip(), wl.strip()
            # skip the title
            if 'Date' in dt:
                continue
            # get the first datetime from the first record
            if not is_date_ok:
                t1 = datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
                is_date_ok = True
            try:
                temp = float(temp)
                wl = float(wl)
                wls = float(wls)
                ws = float(ws)
                wd = float(wd)
                wg = float(wg)
            except ValueError as e:
                # last_wl = 99999
                temp =  wl = wls = ws = wd = wg = 99999
                # wl = 99999
                filling_cnt += 1
            ori_list.append([temp, wl, wls, ws, wd, wg])
            # last_wl = wl

    print(target_file, len(ori_list), filling_cnt/len(ori_list))

    # downsampling
    tailed_idx = len(ori_list) % downsample_factor
    if tailed_idx == 0:
        calc_list = ori_list
    else:
        calc_list = ori_list[:-tailed_idx]
    data_filled = np.array(calc_list).reshape(-1, downsample_factor).mean(axis=1)
    std = statistics.stdev(data_filled)
    mean = sum(data_filled)/len(data_filled)
    low_bound = mean - std*2
    up_bound = mean + std*2
    #info = '{:.2f} {:.2f} {:.2f} {:.2f} {}'.format(std, low_bound, mean, up_bound, filling_cnt)
    #print(info)

    # Data Cleaning: decimate outside plus and minus two standard deviations of mean
    data_cleaned = np.array(data_filled)
    for i,v in enumerate(data_filled):
        if v > up_bound:
            data_cleaned[i] = up_bound
        elif v < low_bound:
            data_cleaned[i] = low_bound

    return data_cleaned, t1

def output_csv_with_date(ori_file, new_data, t1):
    if 'test' in ori_file:
        target_file = '/home/ak/Documents/DataAnalysis/DataAnalysis/DataAnalysis/BHPtest_by_hour.csv'
    else:
        target_file = '/home/ak/Documents/DataAnalysis/DataAnalysis/DataAnalysis/BHPtraining_by_hour.csv'

    if os.path.isfile(target_file):
        os.remove(target_file)
    with open(target_file, 'a+', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['datetime', 'water level'])
        t = t1
        for v in new_data:
            date = t.strftime('%Y-%m-%d %H:%M:%S')
            row_format = [date, round(v, 3)]
            spamwriter.writerow(row_format)
            t = t + datetime.timedelta(hours=12)

def main():
    factor = 10 * 12 # 6 mins * (10) * 12 = 12 hours
    for file_name in ['/home/ak/Documents/DataAnalysis/DataAnalysis/DataAnalysis/BHPtraining.csv', '/home/ak/Documents/DataAnalysis/DataAnalysis/DataAnalysis/BHPtest.csv']:
        new_data, t1 = data_resampling(file_name, factor)
        output_csv_with_date(file_name, new_data, t1)

if __name__ == '__main__':
    main()


