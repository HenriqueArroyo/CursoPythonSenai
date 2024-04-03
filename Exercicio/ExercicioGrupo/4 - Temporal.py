from datetime import datetime
import matplotlib.pyplot as plt

# Dados das vendas
vendas = [
   {"id": 1, "data": "2023-01-05", "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 101},
{"id": 2, "data": "2023-02-12", "produto": "Ofurô", "quantidade": 1, "preco_unitario": 3000.00, "cliente_id": 113},
{"id": 3, "data": "2023-03-20", "produto": "Spa", "quantidade": 3, "preco_unitario": 5000.00, "cliente_id": 103},
{"id": 4, "data": "2023-04-10", "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 104},
{"id": 5, "data": "2023-05-15", "produto": "Ofurô", "quantidade": 2, "preco_unitario": 3000.00, "cliente_id": 105},
{"id": 6, "data": "2023-06-25", "produto": "Spa", "quantidade": 2, "preco_unitario": 5000.00, "cliente_id": 106},
{"id": 7, "data": "2023-07-05", "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 113},
{"id": 8, "data": "2023-08-18", "produto": "Ofurô", "quantidade": 3, "preco_unitario": 3000.00, "cliente_id": 108},
{"id": 9, "data": "2023-09-30", "produto": "Spa", "quantidade": 1, "preco_unitario": 5000.00, "cliente_id": 109},
{"id": 10, "data": "2023-10-08", "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 110},
{"id": 11, "data": "2023-11-12", "produto": "Ofurô", "quantidade": 1, "preco_unitario": 3000.00, "cliente_id": 111},
{"id": 12, "data": "2023-12-20", "produto": "Spa", "quantidade": 3, "preco_unitario": 5000.00, "cliente_id": 112},
{"id": 13, "data": "2023-01-05", "produto": "Banheira", "quantidade": 3, "preco_unitario": 2500.00, "cliente_id": 101},
{"id": 14, "data": "2023-02-12", "produto": "Ofurô", "quantidade": 1, "preco_unitario": 3000.00, "cliente_id": 102},
{"id": 15, "data": "2023-03-20", "produto": "Spa", "quantidade": 2, "preco_unitario": 5000.00, "cliente_id": 103},
{"id": 16, "data": "2023-04-10", "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 104},
{"id": 17, "data": "2023-05-15", "produto": "Ofurô", "quantidade": 3, "preco_unitario": 3000.00, "cliente_id": 105},
{"id": 18, "data": "2023-06-25", "produto": "Spa", "quantidade": 1, "preco_unitario": 5000.00, "cliente_id": 106},
{"id": 19, "data": "2023-07-05", "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 107},
{"id": 20, "data": "2023-08-18", "produto": "Ofurô", "quantidade": 2, "preco_unitario": 3000.00, "cliente_id": 108},
{"id": 21, "data": "2023-09-30", "produto": "Spa", "quantidade": 3, "preco_unitario": 5000.00, "cliente_id": 109},
{"id": 22, "data": "2023-10-08", "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 113},
{"id": 23, "data": "2023-11-12", "produto": "Ofurô", "quantidade": 2, "preco_unitario": 3000.00, "cliente_id": 111},
{"id": 24, "data": "2023-12-20", "produto": "Spa", "quantidade": 1, "preco_unitario": 5000.00, "cliente_id": 112},
{"id": 25, "data": "2023-01-05", "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 113},
{"id": 26, "data": "2023-02-12", "produto": "Ofurô", "quantidade": 3, "preco_unitario": 3000.00, "cliente_id": 102},
{"id": 27, "data": "2023-03-20", "produto": "Spa", "quantidade": 1, "preco_unitario": 5000.00, "cliente_id": 103},
{"id": 28, "data": "2023-04-10", "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 113},
{"id": 29, "data": "2023-05-15", "produto": "Ofurô", "quantidade": 2, "preco_unitario": 3000.00, "cliente_id": 105},
{"id": 30, "data": "2023-06-25", "produto": "Spa", "quantidade": 2, "preco_unitario": 5000.00, "cliente_id": 106},
{"id": 31, "data": "2023-07-05", "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 113},
{"id": 32, "data": "2023-08-18", "produto": "Ofurô", "quantidade": 3, "preco_unitario": 3000.00, "cliente_id": 108},
{"id": 33, "data": "2023-09-30", "produto": "Spa", "quantidade": 1, "preco_unitario": 5000.00, "cliente_id": 109},
{"id": 34, "data": "2023-10-08", "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 113},
{"id": 35, "data": "2023-11-12", "produto": "Ofurô", "quantidade": 1, "preco_unitario": 3000.00, "cliente_id": 111},
{"id": 36, "data": "2023-12-20", "produto": "Spa", "quantidade": 3, "preco_unitario": 5000.00, "cliente_id": 112},
{"id": 37, "data": "2023-01-05", "produto": "Banheira", "quantidade": 3, "preco_unitario": 2500.00, "cliente_id": 101},
{"id": 38, "data": "2023-02-12", "produto": "Ofurô", "quantidade": 1, "preco_unitario": 3000.00, "cliente_id": 102},
{"id": 39, "data": "2023-03-20", "produto": "Spa", "quantidade": 2, "preco_unitario": 5000.00, "cliente_id": 103},
{"id": 40, "data": "2023-04-10", "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 104},
{"id": 41, "data": "2023-05-15", "produto": "Ofurô", "quantidade": 3, "preco_unitario": 3000.00, "cliente_id": 113},
{"id": 42, "data": "2023-06-25", "produto": "Spa", "quantidade": 1, "preco_unitario": 5000.00, "cliente_id": 106},
{"id": 43, "data": "2023-07-05", "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 113},
{"id": 44, "data": "2023-08-18", "produto": "Ofurô", "quantidade": 2, "preco_unitario": 3000.00, "cliente_id": 108},
{"id": 45, "data": "2023-09-30", "produto": "Spa", "quantidade": 3, "preco_unitario": 5000.00, "cliente_id": 109},
{"id": 46, "data": "2023-10-08", "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 110},
{"id": 47, "data": "2023-11-12", "produto": "Ofurô", "quantidade": 2, "preco_unitario": 3000.00, "cliente_id": 113},
{"id": 48, "data": "2023-12-20", "produto": "Spa", "quantidade": 1, "preco_unitario": 5000.00, "cliente_id": 112},
{"id": 49, "data": "2023-01-05", "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 101},
{"id": 50, "data": "2023-02-12", "produto": "Ofurô", "quantidade": 3, "preco_unitario": 3000.00, "cliente_id": 102},
{"id": 51, "data": "2023-03-20", "produto": "Spa", "quantidade": 1, "preco_unitario": 5000.00, "cliente_id": 103},
{"id": 52, "data": "2023-04-10", "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 113},
{"id": 53, "data": "2023-05-15", "produto": "Ofurô", "quantidade": 2, "preco_unitario": 3000.00, "cliente_id": 105},
{"id": 54, "data": "2023-06-25", "produto": "Spa", "quantidade": 2, "preco_unitario": 5000.00, "cliente_id": 106},
{"id": 55, "data": "2023-07-05", "produto": "Banheira", "quantidade": 1, "preco_unitario": 2500.00, "cliente_id": 107},
{"id": 56, "data": "2023-08-18", "produto": "Ofurô", "quantidade": 3, "preco_unitario": 3000.00, "cliente_id": 108},
{"id": 57, "data": "2023-09-30", "produto": "Spa", "quantidade": 1, "preco_unitario": 5000.00, "cliente_id": 109},
{"id": 58, "data": "2023-10-08", "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 113},
{"id": 59, "data": "2023-11-12", "produto": "Ofurô", "quantidade": 1, "preco_unitario": 3000.00, "cliente_id": 111},
{"id": 60, "data": "2023-12-20", "produto": "Spa", "quantidade": 3, "preco_unitario": 5000.00, "cliente_id": 112},



]

# Organizar as vendas por mês
vendas_por_mes = {}
for venda in vendas:
    data = datetime.strptime(venda["data"], '%Y-%m-%d')
    mes = data.strftime("%Y-%m")
    if mes not in vendas_por_mes:
        vendas_por_mes[mes] = 0
    vendas_por_mes[mes] += venda["quantidade"]

# Extrair os meses e as vendas para plotagem
meses = list(vendas_por_mes.keys())
quantidades = list(vendas_por_mes.values())

# Plotar o gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(meses, quantidades, marker='o', linestyle='-')
plt.title('Evolução das vendas ao longo do tempo')
plt.xlabel('Mês')
plt.ylabel('Quantidade de vendas')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
