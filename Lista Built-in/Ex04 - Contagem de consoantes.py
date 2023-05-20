#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor = ["a", "c", "e", "t", "y", "p", "j", "r", "o", "m"]
contador = 0
consoantes = []

#solução1
for caractere in vetor:
    if caractere != "a" and caractere != "e" and caractere != "i" and caractere != "o" and caractere != "u":
        contador += 1
        consoantes.append(caractere)

print(consoantes)

#solução2
for caractere in vetor:
    if caractere not in "aeiou":
        contador += 1
        consoantes.append(caractere)

print(consoantes)