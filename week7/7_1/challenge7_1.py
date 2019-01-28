# coding: utf-8
import numpy as np
import pandas as pd

def co2():
    data = pd.read_excel('ClimateChange.xlsx',sheetname='Data',header=0)

    country = pd.read_excel('ClimateChange.xlsx',sheetname='Country',header=0)
    
    series =  pd.read_excel('ClimateChange.xlsx',sheetname='Series',header=0)
    
    data_co2 = data[data['Series code'] == 'EN.ATM.CO2E.KT']
    data_co2 = data_co2.replace('..',np.nan)
    data_co2 = data_co2.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    data_co2.index = country.index
    
    data_m = pd.concat([data_co2,country],axis=1)
    
    data_m['Sum emissions'] = data_m.sum(axis=1)
    
    data_sum = data_m.iloc[:,[1,-1,-3]]
    print('data_sum:')
    print(data_sum)
    
    data_t = data_sum.groupby(by='Income group').sum()
    
    data_t['Highest emissions country'] = data_sum['Country name'].groupby(data_sum['Income group']).max()
    
    data_t['Highest emissions'] = data_sum['Sum emissions'].groupby(data_sum['Income group']).max()
    
    data_t['Lowest emissions country'] = data_sum['Country name'].groupby(data_sum['Income group']).min()
    
    data_t['Lowest emissions'] = data_sum['Sum emissions'].groupby(data_sum['Income group']).min()

    return data_t


if __name__ == '__main__':
    data_t = co2()
    print(data_t)



