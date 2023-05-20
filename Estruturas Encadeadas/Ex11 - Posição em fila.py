#Crie uma função de busca em que o usuário insere um valor (inteiro)
#e o programa retorna a sua posição na fila.

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

fila1 = Fila()
fila1.insere(1)
fila1.insere(2)
fila1.insere(3)
fila1.insere(4)
#print(fila1)

def Busca_posicao(fila, valor):
    atual = fila.primeiro
    posicao = 0
    while atual and atual.dado != valor:
        atual = atual.proximo
        posicao =+ 1
    return atual.dado, posicao

print("O valor e a sua respectiva posição na fila são: ", Busca_posicao(fila1, 3))