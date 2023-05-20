#Faça um Programa que peça a idade e a altura de 5 pessoas,
#armazene cada informação no seu respectivo vetor.
#Imprima a idade e a altura na ordem inversa a ordem lida.

numeroPessoas = 5
idades = []
alturas = []

for i in range(1, 6):
    print(f"\nOs dados da pessoa {i} são: \n")
    resposta1 = int(input(f"Digite a idade da pessoa {i}: "))
    resposta2 = float(input(f"Digite a idade da pessoa {i}: "))
    idades.append(resposta1)
    alturas.append(resposta2)
print(f"As idades são respectivamente: {idades} e na ordem inversa {idades[::-1]}")
print(f"As alturas são respectivamente: {alturas} e na ordem inversa {alturas[::-1]}")





