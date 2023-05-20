#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
#O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor
#que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
#Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes
#intervalos de valores:
#$200 - $299; $300 - $399; $400 - $499; $500 - $599; $600 - $699; $700 - $799; $800 - $899; $900 - $999; $1000 em diante;

import random
vendedores = int(input('Quantos vendedores a loja tem? '))
salarios = []
vendas = []

#Inserção de dados aleatórios para as vendas

for i in range(vendedores):
    venda = vendas.append(random.randrange(2500,9000))
    salarios.append(200 + vendas[i]*0.09)

print(f"Os valores vendidos nesse mês foram: {vendas}")
print(f"Os salários dos funcionários são: {salarios}")

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0

#Contagem dos salários por faixa de valor

for i in range(len(salarios)):
    if salarios[i] < 299:
        a += 1
    elif salarios[i] < 399:
        b += 1
    elif salarios[i] < 499:
        c += 1
    elif salarios[i] < 599:
        d += 1
    elif salarios[i] < 699:
        e += 1
    elif salarios[i] < 799:
        f += 1
    elif salarios[i] < 899:
        g += 1
    elif salarios[i] < 999:
        h += 1
    elif salarios[i] > 1000:
        i += 1

#Impressão dos resultados

print(f"O número de vendedores na faixa 200-299 dolares: {a}")
print(f"O número de vendedores na faixa 300-399 dolares: {b}")
print(f"O número de vendedores na faixa 400-499 dolares: {c}")
print(f"O número de vendedores na faixa 500-599 dolares: {d}")
print(f"O número de vendedores na faixa 600-699 dolares: {e}")
print(f"O número de vendedores na faixa 700-799 dolares: {f}")
print(f"O número de vendedores na faixa 800-899 dolares: {g}")
print(f"O número de vendedores na faixa 900-999 dolares é: {h}")
print(f"O número de vendedores com salário maior que 1000 dolares é: {h}")