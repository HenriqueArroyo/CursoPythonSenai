# 1 - Variáveis e Operações com Números:

import cmath  # Módulo para lidar com números complexos

# Exercício 1
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Fórmula de Bhaskara
delta = cmath.sqrt(b**2 - 4*a*c)
raiz1 = (-b + delta) / (2*a)
raiz2 = (-b - delta) / (2*a)

print(f"As raízes da equação quadrática são: {raiz1} e {raiz2}")

# Exercício 2
dolares = float(input("Digite o valor em dólares: "))
taxa_conversao = float(input("Digite a taxa de conversão: "))

euros = dolares * taxa_conversao
libras = dolares * 0.75  # Considerando uma taxa de conversão fictícia

print(f"Em euros: {euros:.2f}")
print(f"Em libras: {libras:.2f}")

# 2 - Manipulação de Strings:

# Exercício 3
def palindromo(texto):
    texto = texto.lower().replace(" ", "")  # Remover espaços e converter para minúsculas
    return texto == texto[::-1]

frase_usuario = input("Digite uma frase para verificar se é um palíndromo: ")
resultado_palindromo = palindromo(frase_usuario)
print(f"A frase é um palíndromo: {resultado_palindromo}")

# Exercício 4
frase_usuario = input("Digite uma frase: ")
palavras = frase_usuario.split()
palavra_mais_longa = max(palavras, key=len)
print(f"A palavra mais longa na frase é: {palavra_mais_longa}")


# 3 - Utilização de Listas e Tuplas:

# Exercício 5
def numeros_primos(lista):
    return [num for num in lista if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

numeros = [2, 5, 8, 11, 15, 18, 23]
primos = numeros_primos(numeros)
print(f"Números primos na lista: {primos}")

# Exercício 6
fila_atendimento = []

def adicionar_cliente(nome):
    fila_atendimento.append(nome)

def remover_cliente():
    if fila_atendimento:
        cliente_removido = fila_atendimento.pop(0)
        print(f"Cliente {cliente_removido} foi atendido.")
    else:
        print("Fila vazia. Nenhum cliente para atender.")

def mostrar_posicao_cliente(nome):
    if nome in fila_atendimento:
        posicao = fila_atendimento.index(nome) + 1
        print(f"O cliente {nome} está na posição {posicao} da fila.")
    else:
        print(f"O cliente {nome} não está na fila.")

adicionar_cliente("Alice")
adicionar_cliente("Bob")
adicionar_cliente("Charlie")
mostrar_posicao_cliente("Bob")
remover_cliente()


# 4 - Uso de Operadores Lógicos em Estruturas Condicionais:

# Exercício 7
import random

numero_aleatorio = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Faça um palpite: "))
    tentativas += 1

    if abs(palpite - numero_aleatorio) <= 10:
        print("Está quente!")
    else:
        print("Está frio.")

    if palpite == numero_aleatorio:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break

# Exercício 8
def calculadora():
    operacao = input("Escolha a operação (+, -, *, /, **, sqrt): ")

    if operacao == "sqrt":
        num = float(input("Digite um número para a raiz quadrada: "))
        resultado = num**0.5
    else:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        elif operacao == "**":
            resultado = num1 ** num2
        else:
            print("Operação inválida.")
            return

    print(f"Resultado: {resultado}")

calculadora()