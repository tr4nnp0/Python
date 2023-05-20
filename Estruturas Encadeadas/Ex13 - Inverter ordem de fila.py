#Escreva uma função que inverta a ordem dos elementos da fila.  Por exemplo:
#[1] [4] [5] [2] → [2] [5] [4] [1]

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

    """Foi criado um método para inserir elementos no início em vez do fim"""

    def insere_no_comeco(self, novo_dado):
        """Insere um elemento no final da fila"""

        #Cria um nodo com o novo dado a ser armazenado
        novo_nodo = NodoFila(novo_dado)
        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            # Faz com que o novo nodo seja o último da fila
            novo_nodo.proximo = self.primeiro
            self.primeiro = novo_nodo

    def remove(self):
        """Remove o último elemento da fila"""

        assert self.primeiro != None, "Impossível remover elemento de fila vazia"

        self.primeiro = self.primeiro.proximo
        if self.primeiro == None:
            self.ultimo = None


fila4 = Fila()
fila5 = Fila()

for i in range(6):
    fila4.insere(i)

print(fila4)

def Inverter(fila, fila_invertida):
    elemento = fila.primeiro
    while elemento:
        fila_invertida.insere_no_comeco(elemento.dado)
        elemento = elemento.proximo
    return fila_invertida
print(Inverter(fila4, fila5))



