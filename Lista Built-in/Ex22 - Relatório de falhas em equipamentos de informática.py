"""Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer
um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se
encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número
indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero
encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%"""

#Declaração dos valores

mouses = 4*[0]
erros = ['necessita da esfera', 'necessita da limpeza', 'necessita trocar do cabo ou conector', 'quebrado ou inutilizado']
erro = 1

#Insert dos valores de modelos e dos tipos de defeito

while True:
    while True:
        erro = int(input("Insira o tipo de erro encontrado de 1-4: "))
        if erro < 0 or erro > 4:
            print("Opção inválida.")
        else:
            break

    if erro == 0:
        break
    mouses[erro - 1] = mouses[erro - 1] + 1

    print(mouses)

#Impressão do relatório com os dados finais

cont = 0
print("Situação                               Quantidade        Percentual")
for i in mouses:
    percentual = (i*100)/sum(mouses)
    print(f"{erros[cont]},                    {i},               {percentual:.1f}")
    cont = cont + 1



