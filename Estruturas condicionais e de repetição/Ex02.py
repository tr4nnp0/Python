#Escreva um programa que calcule o valor da hipotensa de um triangulo retângulo, dado o valor de cada um dos catetos.

import math
a = int(input("Digite o valor do primeiro cateto: "))
b = int(input("Digite o valor do segundo cateto: "))
c = math.sqrt(a**2 + b**2)
print("O valor da hipotenusa do triângulo é: ", c)

