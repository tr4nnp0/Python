#Faça um programa que receba a temperatura média de cada mês do ano
#e armazene-as em uma lista. Após isto, calcule a média anual das
#temperaturas e mostre todas as temperaturas acima da média anual,
#e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro,
#2 – Fevereiro, . . . ).

import random
temperaturas = []
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
temperaturas_altas = []
meses_temperaturas_altas = []

for i in range(12):
    temp = temperaturas.append(random.randrange(15,40))

print(f"As temperaturas são: {temperaturas}")

media_anual = sum(temperaturas) / len(temperaturas)

print(f"A média das temperaturas é: {media_anual}")

for i in range(len(temperaturas)):
    if temperaturas[i] > media_anual:
        temperaturas_altas.append(temperaturas[i])
        meses_temperaturas_altas.append(meses[i])

print(f"As temperaturas mais altas do ano são: {temperaturas_altas}")

print("As temperaturas e seus respectivos meses: \n")

for i in range(len(temperaturas_altas)):
    print(f"{temperaturas_altas[i]} - {meses_temperaturas_altas[i]}")


