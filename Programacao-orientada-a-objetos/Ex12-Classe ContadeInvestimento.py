"""Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria,
  com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial
  como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
  Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%.
  Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante."""

class contadeInvestimento:
    def __init__(self, saldo = 1000, taxadejuros = 0.1):
        self.saldo = saldo
        self.taxadejuros = taxadejuros

    def adicioneJuros(self):
        self.saldo +=  self.saldo*self.taxadejuros

    def imprimirSaldo(self):
        return self.saldo

contaTeste = contadeInvestimento()
contaTeste.adicioneJuros()
contaTeste.adicioneJuros()
contaTeste.adicioneJuros()
contaTeste.adicioneJuros()
contaTeste.adicioneJuros()
saldo_final = contaTeste.imprimirSaldo()
print(saldo_final)