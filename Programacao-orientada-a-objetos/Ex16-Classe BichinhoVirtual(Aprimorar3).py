"""Crie uma porta escondida no programa do bichinho virtual, que mostre os valores exatos
dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada
no menu, for informada na escolha do usuário. Dica: acrescente um metodo especial str() à classe
Bichinho."""

class Tamagushi:
    def __init__(self, nome, fome, saude, idade, tempo: float, comida = 0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.comida = comida
        self.tempo = tempo

    def alterarNome(self):
        self.nome = input("Insira o novo nome do seu bichinho: ")

    def retornarNome(self):
        print(f"O nome do seu bichinho virtual foi alterado para: {self.nome}")

    def alimentar(self, comida):
        #comida = int(input("Insira um valor para alimentar seu bichinho: "))
        self.fome = self.fome - comida

    def retornarFome(self):
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

    def brincar(self, tempo):
        self.tempo = tempo

    def humor(self):
        if self.fome > 35 and 0 < self.tempo < 1.5:
            print(f"O {self.nome} está infeliz, com fome e entediado")
        elif 0 < self.fome < 35 and 0 < self.tempo < 1.5:
            print(f"O {self.nome} está saciado, mas está entediado")
        elif self.fome > 35 and self.tempo > 1.5:
            print(f"O {self.nome} está bem humorado, mas com fome. Alimente-o!")
        else:
            print(f"O {self.nome} está bem alimentado e de bom humor! Parabéns!")

    def str(self):
        print(f"Os atributos do seu bichinho são: {self.nome, self.fome, self.saude, self.idade, self.tempo, self.comida}")

bichinhoVirtual1 = Tamagushi("Totoro", 50, 25, 3, 3)
bichinhoVirtual2 = Tamagushi("Snorlax", 35, 32, 4, 1.5)
bichinhoVirtual3 = Tamagushi("Pikachu", 65, 44, 5, 2)

lista = []
lista.append(bichinhoVirtual1)
lista.append(bichinhoVirtual2)
lista.append(bichinhoVirtual3)

while True:
    escolha = int(input("1 - Alimentar os bichinhos da fazenda \n 2 - Brincar com os bichinhos da fazenda \n 3 - Exibir o estado de humor dos seus bichinhos\n 4 - Sair \n Escolha uma opção do menu: "))

    if escolha == 1:
        alimento = int(input("alimentar todos com a quantidade igual a: "))
        for bichinho in range(3):
            lista[bichinho].alimentar(alimento)
        bichinhoVirtual1.str()
        bichinhoVirtual2.str()
        bichinhoVirtual3.str()
    elif escolha == 2:
        tempo = int(input("Brincar com os bichinnhos pela quantidade de horas igual a: "))
        for bichinho in range(3):
            lista[bichinho].brincar(tempo)
        bichinhoVirtual1.str()
        bichinhoVirtual2.str()
        bichinhoVirtual3.str()
    elif escolha == 3:
        for bichinho in range(3):
            lista[bichinho].humor()

    elif escolha == 4:
        print("Hasta la vista, baby!")
        break
