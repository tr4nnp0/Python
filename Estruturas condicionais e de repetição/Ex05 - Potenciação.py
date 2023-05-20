#Elabore um programa que calcule e imprima o valor de xn.
#O valor de n deverá ser maior do que 1 e inteiro e o valor
#de x deverá ser maior ou igual a 2 e inteiro. O cálculo da
#potência deve ser feito sem o uso de funções da biblioteca de math.

x = input("Para calcular o valor de x**n, digite o valor de x: ")
n = input("Digite o valor de n: ")

try:
    int_x = int(x)
    int_n = int(n)
    if int_x >= 2 and int_n >1:
        potencia = int_x**int_n
        print(potencia)
    else:
        print("Digite valores maiores ou iguais a 2 para x e maiores que 1 para n!")
except:
    print("Digite valores inteiros para x e n")


