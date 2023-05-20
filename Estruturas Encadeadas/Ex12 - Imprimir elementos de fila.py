#Crie uma função que percorre e imprime todos os elementos da fila.

class NodoFila:
    """Essa classe representa um nodo de uma lista encadeada"""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)
class Fila:
    """Esta classe representa uma lista encadeada"""
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def insere(self, novo_dado):
        """Insere um elemento no final da fila"""

        #Cria um nodo com o novo dado a ser armazenado
        novo_nodo = NodoFila(novo_dado)
        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            # Faz com que o novo nodo seja o último da fila
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def remove(self):
        """Remove o último elemento da fila"""

        assert self.primeiro != None, "Impossível remover elemento de fila vazia"

        self.primeiro = self.primeiro.proximo
        if self.primeiro == None:
            self.ultimo = None

fila3 = Fila()

for i in range(6):
    fila3.insere(i)

#print(fila3)
...
def Exibir(fila, valor):
    atual = fila.primeiro
    while atual and atual.dado != valor:
        atual = atual.proximo
    return atual

for i in range(7):
    elemento = Exibir(fila3, i)
    if elemento:
        print("Elemento da fila: {0}" .format(i))
