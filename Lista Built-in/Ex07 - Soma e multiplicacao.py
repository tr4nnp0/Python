#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetor = [1, 2, 3, 4, 5]
print(vetor)
print(f"A soma dos elementos do vetor são: {sum(vetor)}")

multi = 0
somamulti = 0
for i in vetor:
    multi = i*(i+1)
    somamulti += multi

print(f"A multiplicação dos elementos do vetor: {somamulti}")
