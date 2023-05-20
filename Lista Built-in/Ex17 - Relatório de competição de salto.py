#Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
#O resultado do atleta será determinado pela média dos cinco valores restantes.
#Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
#pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
#O programa deve ser encerrado quando não for informado o nome do atleta. A saída do
#programa deve ser conforme o exemplo abaixo:
#Atleta: Rodrigo Curvêllo
#Primeiro Salto: 6.5 m;
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m

#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m

import random
atleta = ["Primeiro salto", "Segundo salto", "Terceiro salto", "Quarto salto", "Quinto salto"]
saltos = []

#Inserção de dados aleatórios dos valores dos saltos

for i in range(5):
    saltos.append(random.uniform(5, 6.5))

#Calculo da média dos saltos

media = sum(saltos)/len(saltos)

print("Atleta: Rodrigo Curvello")

#Impressão dos resultados

for i in range(len(atleta)):
    print(f"{atleta[i]}: {saltos[i]} m")

print("Resultado final: ")
print("Atleta: Rodrigo Curvello")
print(f"{round(saltos[0],1)} - {round(saltos[1],1)} - {round(saltos[2],1)} - {round(saltos[3],1)} - {round(saltos[4],1)}")
print(f"Média dos saltos: {round(media,1)} m")
