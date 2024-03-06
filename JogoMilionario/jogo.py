from perguntas import perguntas_e_respostas
import random


premio_inicial = 1000  # Valor inicial do prêmio
progressao_linear = 1000  # Incremento linear do prêmio

perguntas_embaralhadas = list(perguntas_e_respostas.items())
random.shuffle(perguntas_embaralhadas)

pontuacao = 0
for pergunta, resposta_correta in perguntas_embaralhadas:
    print(pergunta)
    resposta_usuario = input("Escolha a opção correta (A, B ou C): ").lower()

    if resposta_usuario == resposta_correta:
        print(f"Resposta correta!\n Você se encontra com {pontuacao} reais.")
        pontuacao += premio_inicial
        premio_inicial += progressao_linear
    else:
        print(f"Resposta incorreta. Sua pontuação final é: {pontuacao} reais.")
        break

print(f"Parabéns! Você ganhou {pontuacao} reais.")