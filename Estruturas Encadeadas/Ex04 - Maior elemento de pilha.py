#Escrever uma função que receba como parâmetro uma pilha.
#A função deve retornar o maior elemento da pilha.

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


def maior_elemento(pilha):
    elemento = pilha.topo
    maior = elemento.dado
    while elemento is not None:
        if elemento.dado > maior:
            maior = elemento.dado
        elemento = elemento.anterior
    return maior

pilha2 = Pilha()
for i in range(5):
    pilha2.insere(i)

print(pilha2)
print(maior_elemento(pilha2))