#Escreva um programa que lê um valor n inteiro e positivo e que
#calcula a seguinte soma: S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n.

num = int(input("Digite um valor inteiro: "))
soma = 0
for i in range(1, num+1):
    termo = 1/i
    print(i)
    print(termo)
    soma = soma + termo

print("A soma de todos os números inseridos é: ", soma)
