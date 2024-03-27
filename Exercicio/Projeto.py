import pandas as pd
import yaml
import matplotlib.pyplot as plt

# Carregar os dados do arquivo YAML
with open('Exercicio/empresa.yaml', 'r') as file:
    dados_yaml = yaml.safe_load(file)

# Converter dados de vendas para DataFrame
df_vendas = pd.DataFrame(dados_yaml['vendas'])

df_cliente = pd.DataFrame(dados_yaml['clientes'])

# Visualizar as primeiras linhas do DataFrame de vendas
print("Primeiras linhas do DataFrame de vendas:")
print(df_vendas.head())
print(df_cliente.head())

