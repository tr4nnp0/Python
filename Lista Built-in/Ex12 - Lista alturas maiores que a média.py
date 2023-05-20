#Foram anotadas as idades e alturas de 30 alunos.
#Faça um Programa que determine quantos alunos com mais de 13 anos
#possuem altura inferior à média de altura desses alunos.

import random

idades = []
alturas = []
maior_de_13 = []
media_13 = []

for i in range(30):
    idade = idades.append(random.randrange(10,17))
    altura = alturas.append(random.randrange(150,180))

for i in range(30):
    if idades[i] > 13:
        maior_de_13.append(alturas[i])

media = sum(maior_de_13)/len(maior_de_13)

for i in range(len(maior_de_13)):
    if maior_de_13[i] < media:
        media_13.append(maior_de_13[i])

print(f"As idades dos alunos são:\n {idades}")
print(f"As alturas dos alunos são: \n {alturas}")
print("A média de altura dos alunos é: %d cm e a quantidade de alunos maiores de 13 anos com altura menor que"
      f"a média de idade dos colegas é: %d alunos" %(media, len(maior_de_13)))