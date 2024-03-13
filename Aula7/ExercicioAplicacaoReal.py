import pandas as pd
import yaml
import matplotlib.pyplot as plt

igm = pd.read_csv('Aula7/igm_modificado.csv')

# print(igm.shape)
# print(igm.info())
# print(igm.head())
# print(igm.tail())
print(igm.sample(5))
# print(igm.sample(5).T)
# print(igm[0:5].T)
# print(igm[-5].T)
# print(igm[['municipio', 'indice_governanca']])
# print(type(igm['porte']))
# print(igm['porte'].value_counts())
# ind_des = igm['indice_governanca']
# print(ind_des.count())
# print(ind_des.size)
# print(ind_des.isnull())
# print(ind_des.isnull().sum())
# print(ind_des.dropna())
# print(ind_des.isnull().sum())
# print(ind_des.dropna(inplace=True))
# print(ind_des.isnull().sum())
# print(ind_des.min())
# print(ind_des.max())
# print(ind_des.std())
# print(ind_des.describe())
# print(igm.describe())
# print(igm[igm['regiao']=='NORDESTE'])