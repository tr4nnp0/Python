#Faça um programa para ler dois inteiros e imprimir o resultado do quadrado da diferença do primeiro valor pelo segundo

int1 = int(input("Insira o primeiro número inteiro: "))
int2 = int(input("Insira o segundo número inteiro: "))

qint1 = int1**2
qint2 = int2**2

diferença = qint1 - qint2
print("O resultado do quadrado da diferença entre o primeiro e o segundo inteiro é: ", diferença)

