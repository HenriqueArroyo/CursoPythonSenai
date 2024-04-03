import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yaml
import numpy as np


with open("empresa.yaml", "r") as file:
    empresa = yaml.safe_load(file)

df_vendas = pd.DataFrame(empresa["vendas"])
df_cliente = pd.DataFrame(empresa["comportamento_do_cliente"])
df_produto = pd.DataFrame(empresa["desempenho_do_produto"])

# Calculando o valor total gasto por cliente
gastos_por_cliente = df_vendas.groupby("cliente_id")["preco_unitario"].sum()

# # Plotando o histograma da distribuição dos gastos dos clientes
plt.figure(figsize=(10, 6))
sns.histplot(gastos_por_cliente, bins=20)
plt.title("Distribuição dos Gastos dos Clientes")
plt.xlabel("Valor Total Gasto")
plt.ylabel("Número de Clientes")
plt.show()

# Identificando os clientes mais fiéis
clientes_mais_fieis = gastos_por_cliente.nlargest(5)

print("Clientes Mais Fiéis:")
print(clientes_mais_fieis)

# Plotando o gráfico de dispersão do valor total gasto versus a frequência de compras
frequencia_de_compras = df_vendas["cliente_id"].value_counts()
plt.figure(figsize=(10, 6))
plt.scatter(frequencia_de_compras, gastos_por_cliente)
plt.title("Valor Total Gasto vs. Frequência de Compras por Cliente")
plt.xlabel("Frequência de Compras")
plt.ylabel("Valor Total Gasto")
plt.show()