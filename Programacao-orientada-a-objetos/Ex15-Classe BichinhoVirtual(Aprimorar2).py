""""Melhore o programa do bichinho virtual, permitindo qu eo usuário especifique
quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho.
Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem."""

class Tamagushi:
    def __init__(self, nome, fome, saude, idade, tempo: float, comida = 0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.comida = comida
        self.tempo = tempo

    def alterarNome(self, nome):
        self.nome = nome

    def retornarNome(self):
        print(f"O nome do seu bichinho virtual foi alterado para: {self.nome}")

    def alimentar(self):
        self.comida = int(input("Insira um valor para alimentar seu bichinho: "))

    def retornarFome(self):
        self.fome = self.fome - self.comida
        if self.fome < 0:
            self.fome = 0;
        print(f"A fome atual do seu bichinho virtual é: {self.fome}")

    def alterarSaude(self):
        self.saude = int(input("Insira um novo valor para saúde do seu bichinho: "))

    def retornarSaude(self):
        print(f"A saude atual do seu bichinho virtual é: {self.saude}")

    def alterarIdade(self):
        self.idade = int(input("Insira um novo valor para a idade do seu bichinho: "))

    def retornarIdade(self):
        print(f"A idade atual do seu bichinho virtual é: {self.idade}")

    def humor(self):
        if self.fome > 35 and 0 < self.tempo < 1.5:
            print("O seu bichinho virtual está infeliz, com fome e entediado")
        elif 0 < self.fome < 35 and 0 < self.tempo < 1.5:
            print("O seu bichinho virtual está saciado, mas está entediado")
        elif self.fome > 35 and self.tempo > 1.5:
            print("O seu bichinho virtual está bem humorado, mas com fome. Alimente-o!")
        else:
            print("O seu bichinho virtual está bem alimentado e de bom humor! Parabéns!")


bichinhoVirtual1 = Tamagushi("Totoro", 50, 25, 3, 3)
bichinhoVirtual1.alterarNome("Ariovaldo")
bichinhoVirtual1.retornarNome()
bichinhoVirtual1.alimentar()
bichinhoVirtual1.retornarFome()
bichinhoVirtual1.alterarSaude()
bichinhoVirtual1.retornarSaude()
bichinhoVirtual1.alterarIdade()
bichinhoVirtual1.retornarIdade()
bichinhoVirtual1.humor()





