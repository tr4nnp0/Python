"""Aprimore a classe do exercício anterior para adicionar o método aumentarSalario(percentualDeAumento)
   que aumento o salário do funcionário em uma certa porcentagem.
   Exemplo de uso:
   harry=funcionario("Harry,25000)
   harry.aumentarSalario(10)"""

class Funcionario:
    def __init__(self, nome: str, salario: float ):
        self.nome = nome
        self.salario = salario

    def mostrarNome(self):
        print(f"O nome do funcionário é: {self.nome}")

    def mostrarSalario(self):
        print(f"O salário de {self.nome} é: {self.salario} reais")

    def aumentarSalario(self, percentual):
        self.salario = self.salario*percentual
        print(f"O salário de {self.nome} com reajuste é {self.salario} reais")

funcionarioTeste = Funcionario("Rubens", 3500)
funcionarioTeste.mostrarNome()
funcionarioTeste.mostrarSalario()
funcionarioTeste.aumentarSalario(1.50)