#No seu sistema operacional ao abrir o “gerenciador de tarefas” você
#pode exibir os processos que estão em execução. Essa funcionalidade
#mantém uma sequência de processos em uma fila, esperando para serem
#executados.
#Seu programa deverá permitir:
#Incluir novos processos na fila de processo;
#Matar o processo com o maior tempo de espera;
#Executar um processo (remover da fila)
#Imprimir o conteúdo da lista de processos.

class Processo:
    def __init__(self, id, nome, prioridade, espera):
        self.id = id
        self.nome = nome
        self.prioridade = prioridade
        self.espera = espera

    def __repr__(self):
        return "%s - %s (prioridade: %s, espera: %s)" %(self.id, self.nome, self.prioridade, self.espera)

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

    def incluir(self, novo_processo):
        """Insere um elemento no final da fila"""
        # Cria um nodo com o novo processo a ser armazenado
        novo_nodo = NodoFila(novo_processo)

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

    def imprimir (self):
        """Imprime todos os elementos da fila"""
        corrente = self.primeiro

        #Percorre a lista de elementps
        while corrente:
            print(corrente.dado)

            #Avança para o próximo nó
            corrente = corrente.proximo

    def remover_maior_espera(self):
        if self.primeiro == None:
            return
        maior_espera = self.primeiro.dado.espera
        nodo_maior_espera = self.primeiro
        corrente = self.primeiro.proximo

        while corrente != None:
            if corrente.dado.espera > maior_espera:
                maior_espera = corrente.dado.espera
                nodo_maior_espera = corrente
            corrente = corrente.proximo

        #Remover o processo com maior espera

        if nodo_maior_espera == self.primeiro:
            self.primeiro = self.primeiro.proximo

        else:
            anterior = self.primeiro
            while anterior.proximo != nodo_maior_espera:
                anterior = anterior.proximo
            anterior.proximo = nodo_maior_espera.proximo
            if nodo_maior_espera == self.ultimo:
                self.ultimo = anterior
        return nodo_maior_espera


