import pandas as pd
import matplotlib.pyplot as plt


serie = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# Acessando elementos por índice
value_at_b = serie['b']
print(value_at_b)


# Fatiando a série
slice_of_series = serie[1:3]
print(slice)

# Operações matemáticas
dobro = serie * 2
print("Série multiplicada por 2:")
print(dobro)

# Filtrando dados
maior_que_30 = serie[serie > 30]
print("Elementos maiores que 30:")
print(maior_que_30)

# Operações estatísticas
media = serie.mean()
soma = serie.sum()
print("Média:", media)
print("Soma:", soma)

data = {'Nome': ['Alice', 'Bob', 'Charlie'],
        'Idade': [25, 30, 35],
        'Cidade': ['A', 'B', 'C']}


df = pd.DataFrame(data)

# Acessando uma coluna por nome
coluna_idade = df['Idade']
print(coluna_idade)


# Selecionando linhas com base em uma condição
linha_filtro = df[df['Idade'] > 30]
print(linha_filtro)


# Adicionando uma nova coluna
df['Profissao'] = ['Engenheiro', 'Analista', 'Designer']
print(df)


# Removendo uma coluna
df_sem_cidade = df.drop('Cidade', axis=1)
print(df_sem_cidade)

# Gráfico de barras da idade por nome
df.plot.bar(x='Nome', y='Idade')
plt.show()

