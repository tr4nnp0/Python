"""Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho
   (estomago) e pelo menos os métodos comer(), verBucho() e digerir().
   Faça um programa ou teste interativamente, criando pelo menos dois macacos,
  alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do
  estomago a cada refeição. Experimente fazer com que um macaco coma o outro.
  É possível criar um macaco canibal?"""

import random

class Macaco:
    def __init__(self, nome, bucho = []):
        self.nome = nome
        self.bucho = bucho

    def comer(self):
        self.bucho.append(input("Digite o primeiro alimento: "))
        self.bucho.append(input("Digite o segundo alimento: "))
        self.bucho.append(input("Digite o terceiro alimento: "))

    def verBucho(self):
        print(self.bucho)

    def digerir(self):
        print(f"O alimento digerido foi: {random.choice(self.bucho)}")

Macaco1 = Macaco("Diddy Kong")
Macaco1.comer()
Macaco1.verBucho()
Macaco1.digerir()


