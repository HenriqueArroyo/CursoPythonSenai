import pandas as pd
import numpy as np
import yaml
import matplotlib.pyplot as plt


# Carregar os dados dos funcionários a partir do arquivo YAML
with open('Exercicio/empresa.yaml', 'r') as file:
    dados_yaml = yaml.safe_load(file)


# Converter para DataFrame
df = pd.DataFrame(dados_yaml['vendas'])

# 1. Análise Exploratória
print("1. Análise Exploratória:")
# print(df.head())  # Visualizar as primeiras linhas
# print(df.info())  # Informações sobre os tipos de dados e valores nulos
# print(df.describe())  # Estatísticas descritivas básicas

