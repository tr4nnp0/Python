#Escreva uma função que receba como parâmetro duas pilhas e verifique de elas são iguais.
#Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem.

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

def pilhas_iguais(p1, p2):
    elemento1 = p1.topo
    elemento2 = p2.topo
    while elemento1 and elemento2 is not None:
        if elemento1.dado == elemento2.dado:
            print("São iguais")
        else:
            print("São diferentes")
        elemento1 = elemento1.anterior
        elemento2 = elemento2.anterior


pilha3 = Pilha()
pilha4 = Pilha()
for i in range(5):
    pilha3.insere(i)
    pilha4.insere(i)

pilha5 = Pilha()
pilha5.insere(4)
pilha5.insere(3)
pilha5.insere(2)
pilha5.insere(1)

print(pilha5)

print(pilha3)
print(pilha4)

pilhas_iguais(pilha3, pilha4)
pilhas_iguais(pilha3, pilha5)


"""Problema não resolvido: Ele entende os valores como iguais, mas não os nodos"""