""""A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar
o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere
 um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma
a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através
de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito
através de uma função, que será chamada pelo programa principal."""

#Declaração dos dados inciais

usuarios = ['alexandre', 'anderson', 'antonio', 'carlos', 'cesar', 'rosemary']
espaco = [456123789, 1245698456, 123456456, 91257581, 987458, 789456125]

#Calculo do percentual

def percentual(parte, total):
    return (parte/total)*100

#Conversão de MB para Bytes

def conversaoMB(byte):
    return byte/1000000

#Impressão dos relatório com o espaço em disco utilizado por cada usuário

print("ACME Inc.                   Uso do espaço em disco pelos usuários")
print("---------------------------------------------------------------------")

print("Nr.   Usuário     Espaço Utilizado      % do do uso")

for i in range(len(espaco)):
    print(f"{i+1}   {usuarios[i]}      {conversaoMB(espaco[i]):.1f}      {percentual(espaco[i],sum(espaco)):.1f}%")

espaco_total = sum(espaco)
espaco_medio = espaco_total/len(espaco)
print(f"Espaço total ocupado: {conversaoMB(espaco_total)}")
print(f"Espaço médio ocupado: {conversaoMB(espaco_medio)}")