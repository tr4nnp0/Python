class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def Engordar(self, peso):
        self.peso += peso

    def Emagrecer(self, peso):
        self.peso -= peso

    def Envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5

    def Crescer(self):
        pass

    def Exibir(self):
        print(f"Nome: {self.nome}, idade: {self.idade} anos, peso: {self.peso} kg, altura: {self.altura} cm")

p1 = Pessoa('Alexandre', 14, 69, 175)
p1.Engordar(1)
p1.Emagrecer(2)
p1.Envelhecer()
p1.Crescer()
p1.Exibir()


