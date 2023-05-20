#1. Implemente a função remove utilizando a função busca.

lista = [1, 2, 3, 4, 5]
def Busca(lista, elemento):
    """Retorna o índice elemento se ele estiver na lista ou None, caso contrário"""
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return None

def Remove(lista, elemento):
    indice = Busca(lista, elemento)
    if indice != None:
        del lista[indice]

elemento = 4
Busca(lista, elemento)
Remove(lista, elemento)
print(f"O elemento {elemento} foi removido da lista resultando em: {lista}")