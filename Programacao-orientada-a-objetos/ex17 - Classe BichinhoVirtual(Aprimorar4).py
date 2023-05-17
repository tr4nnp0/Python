"""Cria uma fazenda de bichinhos instanciando vários objetos bichinho e mantendo o controle
deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de
exigir que o usuário tome conta de um bichinho, exija que ele tome conta da fazenda inteira.
Cada opção do menu deveria permitir que o usuário executasse uma ação para todos
os bichinhos. Para tornar o programa mais interessante, dê para cada bichinho um nível inicial
aleatório de fome e tédio."""

class Tamagushi:
    def __init__(self, nome, fome, saude, idade, comida, horas):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.comida = comida
        self.horas = horas

    def alterarNome(self, nome):
        self.nome = nome

    def retornarNome(self):
        print(f"O nome do seu bichinho virtual foi alterado para: {self.nome}")

    def alterarFome(self):
        if self.comida > 20:
            self.fome = 2*self.comida
        else:
            self.fome += self.comida

    def retornarFome(self):
        print(f"A fome atual do seu bichinho virtual é: {self.fome}")

    def alterarSaude(self, saude):
        if self.comida > 20 and self.horas > 2:
            self.saude = 2*saude
        else:
            self.saude = saude + self.comida

    def retornarSaude(self):
        print(f"A saude atual do seu bichinho virtual é: {self.saude}")

    def alterarIdade(self, idade):
        self.idade = idade

    def retornarIdade(self):
        print(f"A idade atual do seu bichinho virtual é: {self.idade}")

    def brincar(self):
        if self.horas > 2.5:
            self.fome = self.fome*1.2
            self.saude = self.saude*1.2
        else:
            self.fome = self.fome
            self.saude = self.saude

    def humor(self):
        if 0 < self.fome < 25 and 0 < self.saude < 50:
            print("O seu bichinho virtual está infeliz, fome e problemas de saúde")
        elif self.fome > 25 and 0 < self.saude < 50:
            print("O seu bichinho virtual está feliz, mas pode ter problemas de saúde")
        elif 0 < self.fome < 25 and self.saude > 50:
            print("O seu bichinho virtual está feliz, mas com fome. Alimente-o!")
        else:
            print("O seu bichinho virtual está bem alimentado e com saúde! Parabéns!")

bichinhoVirtual = Tamagushi("Totoro", 50, 25, 3, 15, 5)
bichinhoVirtual.alterarNome('Astrogildo')
bichinhoVirtual.retornarNome()
bichinhoVirtual.alterarFome()
bichinhoVirtual.retornarFome()
bichinhoVirtual.alterarSaude(55)
bichinhoVirtual.retornarSaude()
bichinhoVirtual.alterarIdade(5)
bichinhoVirtual.retornarIdade()
bichinhoVirtual.brincar()
bichinhoVirtual.humor()