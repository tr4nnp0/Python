#3.	Vetores estranhos – criei um programa que solicite até 20 números inteiros
#positivos, e os armazene em um vetor. A entrada dos números termina ao chegar
#a 20 ou se o usuário digitar um valor negativo. Ao termina a entrada de dados
#imprima os números, a soma dos números, a quantidade entrada e a média.


matriz = [[0,0,0], [0,0,0], [0,0,0]]
linha_1 = []
linha_2 = []
linha_3 = []

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input("Digite o valor do elemento para a posição [%d][%d]: " %(i+1, j+1)))

for i in range(1):
    for j in range(3):
        linha_1.append(matriz[0][j])

for i in range(1):
    for j in range(3):
        linha_2.append(matriz[1][j])

for i in range(1):
    for j in range(3):
        linha_3.append(matriz[2][j])

linha_1.reverse()
linha_2.reverse()
linha_3.reverse()

soma = matriz[0][0] + matriz[1][1] + matriz[2][2]

print("A matriz é igual = ")
for resultado in matriz:
    print(resultado)

print("O formato invertido da matriz é = ")
print(linha_3)
print(linha_2)
print(linha_1)

print("A soma das diagonais é igual a: ", soma)
