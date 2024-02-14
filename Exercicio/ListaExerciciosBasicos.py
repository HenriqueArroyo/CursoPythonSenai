# Correção da Lista de Exercícios:

# 1 - Variáveis e Operações com Números:

# Exercício 1
a = int(input("Digite um nº"))
b = int(input("Digite outro nº"))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
resto_divisao = a % b
potenciacao = a ** b

# Raio de um círculo
raio = 4
area_circulo = 3.14 * (raio ** 2)

print(soma, subtracao, multiplicacao, divisao, divisao_inteira, resto_divisao, potenciacao)
print(f"A área do círculo com raio {raio} é: {area_circulo}")


# 2 - Manipulação de Strings:

# Exercício 2
nome = str(input("Digite seu Nome: \n"))
sobrenome = str(input("Digite seu Sobrenome: \n"))

nome_completo = nome + " " + sobrenome

frase = "Python é uma linguagem poderosa"
frase_maiusculas = frase.upper()
frase_minusculas = frase.lower()
frase_substituida = frase.replace("poderosa", "incrível")

print(nome_completo)
print(frase_maiusculas)
print(frase_minusculas)
print(frase_substituida)

# 3 - Utilização de Listas e Tuplas:

# Exercício 3
cores = ["azul", "verde", "vermelho"]
cores.extend(["amarelo", "roxo"])

# Exercício 4
coordenadas = (40.7128, -74.0060)
latitude, longitude = coordenadas

print(cores)
print(f"Latitude: {latitude}, Longitude: {longitude}")

# 4 - Uso de Operadores Lógicos em Estruturas Condicionais:

# Exercício 5
tem_sol = True
tem_chuva = False

if tem_sol and not tem_chuva:
    print("É um dia agradável!")
else:
    print("Não é um dia agradável.")

# Exercício 6
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos são números pares.")
else:
    print("Pelo menos um dos números não é par.")

# Exercício 7
numeros = [1, 3, 6, 9, 12, 15]

for numero in numeros:
    if numero % 3 == 0 and numero % 2 != 0:
        print(f"{numero} é múltiplo de 3 e ímpar.")

# Exercício 8
idade = int(input("Digite sua idade: "))

if 18 <= idade <= 65:
    print("Sua idade está dentro do intervalo permitido.")
else:
    print("Sua idade está fora do intervalo permitido.")