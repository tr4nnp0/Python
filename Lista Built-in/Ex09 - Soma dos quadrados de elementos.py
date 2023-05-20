#Faça um Programa que leia um vetor A com 10 números inteiros,
#calcule e mostre a soma dos quadrados dos elementos do vetor.

A = []
quadrado = 0
somaquadrado = 0
for i in range(1,11):
    A.append(i)

print(f"Os elementos do vetor são: {A}")

for i in A:
    quadrado = i*i
    somaquadrado += quadrado

print(f"E a soma dos quadrados desse vetor é: {somaquadrado}")