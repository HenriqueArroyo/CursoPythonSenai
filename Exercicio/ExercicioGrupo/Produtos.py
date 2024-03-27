import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yaml
import numpy as np
import matplotlib.pyplot as plt


with open("empresa.yaml", "r") as file:
    empresa = yaml.safe_load(file)

df_vendas = pd.DataFrame(empresa["vendas"])
df_cliente = pd.DataFrame(empresa["comportamento_do_cliente"])
df_produto = pd.DataFrame(empresa["desempenho_do_produto"])

# Dados dos produtos
produtos = ['Banheira', 'Ofuro', 'Spa']
receita_total = [80000.00, 123000.00, 185000.00]
vendas_totais = [32, 41, 37]

# Plotar gráfico de barras dos produtos mais vendidos
plt.figure(figsize=(10, 6))
plt.bar(produtos, vendas_totais, color='skyblue')
plt.xlabel('Produto')
plt.ylabel('Número de Vendas')
plt.title('Produtos Mais Vendidos')
plt.show()

# Plotar gráfico de pizza da distribuição da receita entre os produtos
plt.figure(figsize=(8, 8))
plt.pie(receita_total, labels=produtos, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribuição da Receita entre os Produtos')
plt.show()
