class quadrado:
    def __init__(self, lado):
        self.lado = lado

    def muda_valor_lado(self, novo_lado):
        self.lado = novo_lado

    def retorna_valor_lado(self):
        print(self.lado)

    def calcular_area(self):
        area = self.lado*self.lado
        print(f'{area}m²')
        return area

q1 = quadrado(7)
q1.muda_valor_lado(10)
q1.retorna_valor_lado()
q1.calcular_area()

