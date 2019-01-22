# -*- coding: utf-8 -*-

import pandas as pd

def quarter_volume():
    data = pd.read_csv('apple.csv')

    data.index = pd.to_datetime(data.Date)

    sort_data = data.Volume.resample('Q').sum().sort_values(ascending=False)

    second_volume = sort_data[1]

    return second_volume

if __name__ == '__main__':
    quarter_volume()
