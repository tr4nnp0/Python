class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        print(self.cor)

Bola1 = Bola('Verde', '20cm', 'Borracha')
print(Bola1.cor, Bola1.circunferencia, Bola1.material)
Bola1.trocaCor('azul')
Bola1.mostraCor()