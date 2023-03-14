class Tamagushi:
    def __init__(self, nome: str, fome: int, saude: int, idade: int):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def Alterar_Nome(self, novo_nome):
        self.nome = novo_nome

    def Retornar_Nome(self):
        print(f"Você alterou o nome do seu Tamagushi para: {self.nome}")

    def Alterar_Fome(self, novo_fome):
        self.fome = novo_fome

    def Retornar_Fome(self):
        print(f"Você alterou o nível de fome do seu Tamagushi para: {self.fome}")

    def Alterar_Saude(self, novo_saude):
        self.saude = novo_saude

    def Retornar_Saude(self):
        print(f"Você alterou o nível de saúde do seu Tamagushi para: {self.saude}")

    def Alterar_Idade(self, novo_idade):
        self.idade = novo_idade

    def Retornar_Idade(self):
        print(f"Você alterou a idade seu Tamagushi para: {self.idade}")

    def Humor(self):
        if self.fome > 20 and self.saude >20:
            print("Seu Tamaguchi, felizmente, está de bom humor!")
        else:
            print("Seu Tamaguchi, infelizmente, não está de bom humor")

    def Mostrar_Atributos(self):
        print(f"Nome: {self.nome}, Fome: {self.fome}, Saúde: {self.saude}, Idade: {self.idade}")


T1 = Tamagushi('Chupa-cabra', 15, 13, 3)
T1.Alterar_Nome('Totoro')
T1.Retornar_Nome()
T1.Alterar_Fome(21)
T1.Retornar_Fome()
T1.Alterar_Saude(10)
T1.Retornar_Saude()
T1.Alterar_Idade(4)
T1.Retornar_Idade()
T1.Humor()
T1.Mostrar_Atributos()



