'''Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque.
 No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
'''

class Conta_Corrente:
    def __init__(self, nome: str, conta: int, saldo: float):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, conta: {self.conta}, saldo: {self.saldo}")

Conta1 = Conta_Corrente('Aderbal', 1453, 500)
Conta1.alterar_nome('Cleonice')
Conta1.deposito(800)
Conta1.saque(400)
Conta1.mostrar_dados()
