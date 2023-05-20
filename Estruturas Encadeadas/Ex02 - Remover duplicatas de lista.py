#Remova duplicatas de uma lista ordenada. Suponha que lhe seja fornecida uma
#lista encadeada armazenando números inteiros em ordem crescente. Sua tarefa é
#remover todos os elementos duplicados da lista. Por exemplo, dada a lista
#[0 → 1 → 1 → 5 → 7 → 10 → 10 → None], seu programa deve retornar a lista
#[0 → 1 → 5 → 7 → 10 → None].


class NodoLista:
    """Essa classe representa um nodo de uma lista encadeada"""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)
class ListaEncadeada:
    """Esta classe representa uma lista encadeada"""
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def insere_no_inicio(lista, novo_dado):
        # 1) Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = NodoLista(novo_dado)

        # 2) Faz com que o novo nodo seja a cabeça da lista.
        novo_nodo.proximo = lista.cabeca

        # 3) Faz com que a cabeça da lista referencie o novo nodo.
        lista.cabeca = novo_nodo

lista_duplicatas = ListaEncadeada()
insere_no_inicio(lista_duplicatas, 10)
insere_no_inicio(lista_duplicatas, 10)
insere_no_inicio(lista_duplicatas, 7)
insere_no_inicio(lista_duplicatas, 5)
insere_no_inicio(lista_duplicatas, 1)
insere_no_inicio(lista_duplicatas, 1)
insere_no_inicio(lista_duplicatas, 0)

print(lista_duplicatas)

def remove_duplicatas(lista):
    corrente = lista.cabeca
    while corrente:
        proximo_distinto = corrente.proximo
        while proximo_distinto and proximo_distinto.dado == corrente.dado:
            proximo_distinto = proximo_distinto.proximo
        corrente.proximo = proximo_distinto
        corrente = proximo_distinto
    return lista

remove_duplicatas(lista_duplicatas)
print(lista_duplicatas)
