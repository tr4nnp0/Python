"""Crie uma classe que modele um retângulo:
Atributos: Comprimento e Altura
Métodos: Mudar valor do lados, Retornar valor dos lados, calcular Área e
calcular Perímetro.
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que
informe as medidas de um local. Depois deve criar um objeto com as medidas
e calcular a quantidade de pisos e rodapés necessários para o local"""

class retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_lados(self, novo_comprimento, novo_largura):
        self.comprimento = novo_comprimento
        self.largura = novo_largura

    def retornar_lados(self):
        print(self.comprimento)
        print(self.largura)

    def calcular_area(self):
        area = self.comprimento*self.largura
        print(f'{area}m²')
        return area

    def calcular_perimetro(self):
        perimetro = 2*self.comprimento + 2*self.largura
        print(f'{perimetro}m')
        return perimetro

y = int(input("Informe o comprimento do local: "))
x = int(input("Informe a largura do local: "))
local = retangulo(x,y)

print(f'Serão necessários {local.calcular_area()}m² de piso e {local.calcular_perimetro()}m de rodapés para suprir o local')

#r1 = retangulo(y,x)
#r1.mudar_lados(y,x)
#r1.retornar_lados()
#r1.calcular_area()
#r1.calcular_perimetro()





