#Construa um programa utilizando uma pilha que resolva o seguinte problema:
#Armazene as placas dos carros (apenas os números) que estão estacionados numa rua sem saída estreita.
#Dado uma placa verifique se o carro está estacionado na rua.
#Caso esteja, informe a sequência de carros que deverá ser retirada para que o carro em questão consiga sair.

class NodoPilha:
    """Essa classe representa um nodo de uma estrutura encadeada"""
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)
class Pilha:
    """Esta classe representa uma pilha usando uma estrutura encadeada"""
    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def insere(self, novo_dado):
        # 1) Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = NodoPilha(novo_dado)

        # 2) Faz com que o novo nodo seja o topo da lista.
        novo_nodo.anterior = self.topo

        # 3) Faz com que a cabeça da lista referencie o novo nodo.
        self.topo = novo_nodo

    def remove(self):
        """Remove o elemento que está no topo da pilha"""
        """Para removero elemento, na prática o nodo não precisa ser apagado, apenas
        alteramos o apontador do topo da pilha"""

        assert self.topo, "Impossível remover valor de pilha vazia"

        self.topo = self.topo.anterior

pilha_placas = Pilha()
pilha_placas.insere(2082)
pilha_placas.insere(2808)
pilha_placas.insere(3680)
pilha_placas.insere(2596)
pilha_placas.insere(2961)


print(pilha_placas)

def busca(pilha, placa):
    corrente = pilha.topo
    while corrente and corrente.dado != placa:
        corrente = corrente.anterior
    print(f"O automóvel com a placa {corrente.dado} está estacionado na rua")

busca(pilha_placas, 3680)

while pilha_placas.topo != None:
    pilha_placas.remove()
    print("A sequência de carros para que o carro em questão consiga sair é: ", pilha_placas)

"""Problema não resolvido: Não consigo pegar no while somente até o carro que quero, mas até o None. Se não dá erro"""