import pandas as pd
import yaml
from ruamel.yaml import YAML

# abrindo o arquivo
with open('empresa.yaml', 'r') as file:
    dados = yaml.safe_load(file) #alocando o arquivo em uma variável(foi carregada como yaml com esquema de tabelas)

# Criando os dataframes para cada tabela e suas colunas
df_vendas = pd.DataFrame(dados['vendas'])   # criando dataframe das vendas
df_clientes = pd.DataFrame(dados['comportamento_do_cliente']) # criando dataframe dos clientes
df_produto = pd.DataFrame(dados['desempenho_do_produto']) # criando dataframe dos produtos

print(df_vendas.describe()), '\n' # Gerando estatísticas descritivas para a tabela de vendas
print(df_clientes.describe()), '\n'  # Gerando estatísticas descritivas para a tabela de clientes
print(df_produto.describe()), '\n'  # Gerando estatísticas descritivas para a tabela de produtos


# total de vendas de banheiras e receita total
acessa_banheira = df_vendas[df_vendas['produto'] == 'Banheira']
total = acessa_banheira['quantidade'].sum() * acessa_banheira['preco_unitario']
# print(total)

# total de vendas de banheiras furadas e receita total
acessa_furada = df_vendas[df_vendas['produto'] == "furado"]
total_furado = acessa_furada['quantidade'].sum()
receita_total_furado = total_furado * acessa_furada['preco_unitario'] 
#print(receita_total_furado)


acessa_spa = df_vendas[df_vendas['produto'] == "Spa"]
total_spa = acessa_spa['quantidade'].sum()
receia_total_spa = total_spa * acessa_spa['preco_unitario']
#print(total_spa)
#print(receita_total_spa)