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