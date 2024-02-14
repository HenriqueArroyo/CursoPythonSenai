idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif 18 <= idade < 60:
    print("Você é adulto.")
else:
    print("Você é um(a) idoso(a).")
