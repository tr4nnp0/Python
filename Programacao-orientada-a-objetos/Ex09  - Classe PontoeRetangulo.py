"""
Classe Ponto e Retangulo:
Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.

A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.

O valor do centro do objeto deve ser mostrado na tela.

Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""

class Retangulo:
    def __init__(self, largura: float,comprimento: float):
        self.largura = largura
        self.comprimento = comprimento

    def Encontrar_Centro(self, c1, c2):
        if self.largura%2 = 0 and self.comprimento%2 = 0:
            c1 = self.largura/2
            c2 = self.comprimento/2
        else:
            c1 = self.largura / 2 + 0.5
            c2 = self.comprimento / 2 + 0.5


class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def Imprimir_Valores(self):
        print(self.x, self.y)

    def Encontrar_Centro(self):
