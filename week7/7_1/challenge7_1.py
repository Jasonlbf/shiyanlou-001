# coding: utf-8
import pandas as pd

def co2():
    data = pd.read_excel('ClimateChange.xlsx',sheetname='Data',header=0)

    country = pd.read_excel('ClimateChange.xlsx',sheetname='Country',header=0)
    
    #series =  pd.read_excel('ClimateChange.xlsx',sheetname='Series',header=0)
    
    data_co2 = data[data['Series code'] == 'EN.ATM.CO2E.KT']
    data_co2 = data_co2.sort_values(by='Country code')
    data_co2.index = data_co2['Country code'] 
    data_co2 = data_co2.drop(['Country code','Country name','Series code','Series name','SCALE','Decimals'],axis=1)

    data_co2 = data_co2.replace('..',pd.np.nan)
    data_co2 = data_co2.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    country = country.sort_values(by='Country code')
    country.index = country['Country code'] 
    data_sum = pd.concat([data_co2.sum(axis=1),country[['Country name','Income group']]],axis=1)
    #data_sum = data_sum.dropna()
    data_sum = data_sum[data_sum[0]>0]
    data_se = data_sum.groupby(by='Income group').sum()
    data_se.columns = ['Sum emissions']
    data_he = data_sum.groupby(by='Income group').apply(lambda t: t[t[0] == t[0].max()])
    data_le = data_sum.groupby(by='Income group').apply(lambda t: t[t[0] == t[0].min()])
    data_he.index=range(len(data_he.values))
    data_he.index = data_he['Income group']
    data_he = data_he.drop(['Income group'],axis=1)
    data_he.columns = ['Highest emissions','Highest emission country']
    data_le.index=range(len(data_le.values))
    data_le.index = data_le['Income group']
    data_le = data_le.drop(['Income group'],axis=1)
    data_le.columns = ['Lowest emissions','Lowest emission country'] 
    data_t = pd.concat([data_se,data_he,data_le],axis=1)

    return data_t


if __name__ == '__main__':
    data_t = co2()
    print(data_t)


