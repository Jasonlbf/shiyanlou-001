# coding: utf-8
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def co2_gdp_plot():
    data = pd.read_excel('ClimateChange.xlsx',sheetname='Data',header=0)

    country = pd.read_excel('ClimateChange.xlsx',sheetname='Country',header=0)
    
    #series =  pd.read_excel('ClimateChange.xlsx',sheetname='Series',header=0)
    
    data_co2 = data[data['Series code'] == 'EN.ATM.CO2E.KT']
    data_gdp = data[data['Series code'] == 'NY.GDP.MKTP.CD']
    data_co2 = data_co2.sort_values(by='Country code')
    data_gdp = data_gdp.sort_values(by='Country code')
    #data_co2 = data_co2[data_co2['Country code'].isin(countrys_list)]
    #data_gdp = data_gdp[data_gdp['Country code'].isin(countrys_list)]
    data_co2.index = data_co2['Country code'] 
    data_gdp.index = data_gdp['Country code'] 
    data_co2 = data_co2.drop(['Country code','Country name','Series code','Series name','SCALE','Decimals'],axis=1)
    data_gdp = data_gdp.drop(['Country code','Country name','Series code','Series name','SCALE','Decimals'],axis=1)

    data_co2 = data_co2.replace('..',pd.np.nan)
    data_gdp = data_gdp.replace('..',pd.np.nan)
    data_co2 = data_co2.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    data_gdp = data_gdp.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
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


