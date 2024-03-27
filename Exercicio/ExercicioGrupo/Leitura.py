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


# Converter a coluna 'data' para o tipo datetime do pandas
df_vendas["data"] = pd.to_datetime(df_vendas["data"])

# Extrair o mês da data e adicionar como uma nova coluna chamada 'mes'
df_vendas["mes"] = df_vendas["data"].dt.month

print(df_vendas.head())

plt.figure(figsize=(10, 6))
sns.barplot(data=df_vendas, x="mes", y="preco_unitario", palette="deep" , estimator=sum)
plt.title("Contagem de Vendas Mensais")
plt.xlabel("Mês")
plt.ylabel("Receita Total")
plt.grid(True)
plt.show()







