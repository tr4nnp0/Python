#Seja a seguinte série: 1, 4, 9, 16, 25, 36, ... Escreva um programa que
#gere esta série até o N-ésimo termo, digitado pelo usuário.

num = int(input("Insira um número para saber todas as potências de 1 a n: "))

for i in range(1, num+1):
    potencia = i**2
    print(potencia)
