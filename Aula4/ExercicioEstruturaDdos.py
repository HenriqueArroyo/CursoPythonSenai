# Manipulação de Listas
lista_numeros = [7, 3, 10, 2, 5]
lista_numeros.sort()  # Ordena a lista em ordem crescente
lista_numeros.append(10)  # Adiciona o número 10 ao final da lista
lista_numeros.remove(5)  # Remove o elemento de valor 5 da lista
print(lista_numeros)

# Slicing e Operações
primeiros_10_numeros = list(range(1, 11))  # Cria uma lista com os primeiros 10 números inteiros
sublista_pares = primeiros_10_numeros[1::2]  # Cria uma sublista com os números pares usando slicing
sublista_pares.reverse()  # Inverte a ordem da sublista
print(sublista_pares)
print(primeiros_10_numeros)


# Listas Aninhadas
cores_hex = [['vermelho', '#FF0000'], ['verde', '#00FF00'], ['azul', '#0000FF']]
codigo_verde = [cor[1] for cor in cores_hex if cor[0] == 'verde']
print(codigo_verde[0])  # Imprime o código hexadecimal da cor verde

# Operações com Tuplas
meses_do_ano = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
primeiros_seis_meses = meses_do_ano[:6]  # Acesse os meses de janeiro a junho
# Tentativa de adicionar um novo mês à tupla (não é possível)

# Tuplas como Chaves de Dicionários
coordenadas_cidades = {(40.7128, -74.0060): 'Nova York', (34.0522, -118.2437): 'Los Angeles', (41.8781, -87.6298): 'Chicago'}
nome_ny = coordenadas_cidades[(40.7128, -74.0060)]  # Acesse e imprima o nome da cidade correspondente à coordenada de Nova York
print(nome_ny)

# Operações de Conjuntos
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}
uniao = conjunto1.union(conjunto2)  # União de conjuntos
intersecao = conjunto1.intersection(conjunto2)  # Interseção de conjuntos
diferenca = conjunto1.difference(conjunto2)  # Diferença de conjuntos
print(uniao)
print
# Remoção de Duplicatas
lista_com_duplicatas = [1, 2, 3, 2, 4, 5, 3, 6]
conjunto_sem_duplicatas = set(lista_com_duplicatas)  # Converte a lista para um conjunto para remover duplicatas

# Manipulação de Dicionários
livro = {'titulo': 'Dom Quixote', 'autor': 'Miguel de Cervantes', 'ano_publicacao': 1605}
livro['num_paginas'] = 863  # Adiciona uma nova chave-valor ao dicionário representando a quantidade de páginas

# Iteração e Impressão
paises_capitais = {'Brasil': 'Brasília', 'EUA': 'Washington D.C.', 'França': 'Paris'}
for pais, capital in paises_capitais.items():
    print(f'A capital de {pais} é {capital}')

# Remoção de Itens
inventario = {'produto1': 10, 'produto2': 20, 'produto3': 15}
del inventario['produto2']  # Remove um item do inventário pelo nome do produto