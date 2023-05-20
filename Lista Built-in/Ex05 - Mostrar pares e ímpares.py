#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
#Imprima os três vetores.

vetor = []
pares = []
impares = []
while True:
    numero = int(input("Digite um número: "))
    vetor.append(numero)
    if len(vetor) == 20:
        break

    if numero%2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"A lista completa dos números é: {vetor}")
print(f"Os pares são: {pares}")
print(f"Os ímpares são: {impares}")

