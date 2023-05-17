"""Implemente a classe Funcionário. Um empregado tem um nome (um string)
 e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos
  para devolver nome e salário. Escreva um pequeno programa que teste sua classe."""

class Funcionario:
    def __init__(self, nome: str, salario: float ):
        self.nome = nome
        self.salario = salario

    def mostrarNome(self):
        print(f"O nome do funcionário é: {self.nome}")

    def mostrarSalario(self):
        print(f"O salário de {self.nome} é: {self.salario} reais")

    #def aumentarSalario(self, percentual):
     #   self.salario = self.salario*percentual
      #  print(f"O salário de {self.nome} com reajuste é {self.salario} reais")

funcionarioTeste = Funcionario("Rubens", 3500)
funcionarioTeste.mostrarNome()
funcionarioTeste.mostrarSalario()
#funcionarioTeste.aumentarSalario(1.50)