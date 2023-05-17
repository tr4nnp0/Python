 """Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
  Atributos: Nome, Fome, Saúde e Idade
  Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
  Obs Existe mais uma informação que devemos levar em consideração,
  o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde,
  ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação
  por que ela pode ser calculada a qualquer momento."""

class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, nome):
        self.nome = nome

    def retornarNome(self):
        print(f"O nome do seu bichinho virtual foi alterado para: {self.nome}")

    def alterarFome(self):
        self.fome = int(input("Insira um novo valor para a fome do seu bichinho: "))

    def retornarFome(self):
        print(f"A fome atual do seu bichinho virtual é: {self.fome}")

    def alterarSaude(self):
        self.saude = int(input("Insira um novo valor para a saúde do seu bichinho: "))

    def retornarSaude(self):
        print(f"A saude atual do seu bichinho virtual é: {self.saude}")

    def alterarIdade(self):
        self.idade = int(input("Insira um novo valor para a idade do seu bichinho: "))

    def retornarIdade(self):
        print(f"A idade atual do seu bichinho virtual é: {self.idade}")

    def humor(self):
        if self.fome > 35 and 0 < self.saude < 50:
            print("O seu bichinho virtual está infeliz, fome e problemas de saúde")
        elif 0 < self.fome < 35 and 0 < self.saude < 50:
            print("O seu bichinho virtual está saciado, mas pode ter problemas de saúde")
        elif self.fome > 35 and self.saude > 50:
            print("O seu bichinho virtual está feliz, mas com fome. Alimente-o!")
        else:
            print("O seu bichinho virtual está bem alimentado e com saúde! Parabéns!")


bichinhoVirtual1 = Tamagushi("Totoro", 50, 25, 3)
bichinhoVirtual1.alterarFome()
bichinhoVirtual1.retornarFome()
bichinhoVirtual1.alterarSaude()
bichinhoVirtual1.retornarSaude()
bichinhoVirtual1.alterarIdade()
bichinhoVirtual1.retornarIdade()
bichinhoVirtual1.humor()





