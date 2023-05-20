#Implemente uma função chamada TPilha, que receba um vetor de inteiros com 15 elementos. Para cada um deles, como segue:
#Se o número for par, insira-o na pilha;
#Se o número lido for ímpar, retire um número da pilha;
#Ao final, esvazie a pilha imprimindo os elementos.

import random

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

vetor = []
for i in range(16):
    vetor.append(random.randrange(1,30))

pilha_par = Pilha()

print(vetor)

def TPilha(vetor, pilha):
    for i in range(len(vetor)):
        if vetor[i]%2 == 0:
            pilha_par.insere(vetor[i])
    print(pilha_par)

TPilha(vetor, pilha_par)