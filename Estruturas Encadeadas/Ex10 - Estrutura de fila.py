# Implemente uma fila dinâmica contendo todas as funcionalidades de uma fila padrão. Para isso, resolvar:
#Crie um nó padrão da fila.
#Crie uma função de inicialização da fila vazia
#Crie uma função push que cria e insere um novo nó para o final da fila.
#Crie uma função pop que remove o primeiro elemento da fila.

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
        novo_nodo = Nodo(novo_dado)
        if self.primeiro = None:
            self.primeiro = novo_nodo
            self.ultimo = novo
        else:
            # Faz com que o novo nodo seja o último da fila
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def remove(self):
        """Remove o último elemento da fila"""

        assert self.primeiro != None, "Impossível remover elemento de fila vazia"

        self.primeiro = self.primeiro.proximo
        if self.primeiro = None:
            self.ultimo = None

    
