# coding: utf-8
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def climate_plot():
    data_climate = pd.read_excel('ClimateChange.xlsx',sheetname='Data',header=0)

    data_tempe = pd.read_excel('GlobalTemperature.xlsx',header=0)
    
    sc_list = ['EN.ATM.CO2E.KT','EN.ATM.METH.KT.CE','EN.ATM.NOXE.KT.CE','EN.ATM.GHGO.KT.CE','EN.CLC.GHGR.MT.CE']

    data_c = [data_climate['Series code'].isin(sc_list)]

    data_c = data_c.drop(['Country code','Country name','Series code','Series name','SCALE','Decimals'],axis=1)

    data_c = data_c.replace('..',pd.np.nan)
    data_c = data_c.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    data_c = data_c.dropna()

    data_sum = pd.concat([data_co2.sum(axis=1),data_gdp.sum(axis=1)],axis=1)
    data_norm = (data_sum - data_sum.min()) / (data_sum.max() - data_sum.min())
    
    data_norm.columns = ['CO2-SUM','GDP-SUM']

    data_china = data_norm[data_norm.index == 'CHN']

    countrys_list = ['CHN','USA','GBR','FRA','RUS']
    sticks_list = []
    labels_pos = []
    for i in range(len(data_norm)):
        if data_norm.index[i] in countrys_list:
            sticks_list.append(data_norm.index[i])
            labels_pos.append(i)


    fig = plt.subplot()
    data_norm.plot(kind='line',title='GDP-CO2',ax=fig)
    plt.xlabel('Countries')
    plt.ylabel('Values')
    plt.xticks(labels_pos, sticks_list, rotation='vertical')
    plt.show()

    return fig, np.round(data_china.values,3).tolist()[0]


if __name__ == '__main__':
    data_t = co2_gdp_plot()
    print(data_t)


