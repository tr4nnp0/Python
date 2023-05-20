"""Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos
valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar
o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos."""

#InserçãoDosDados

sistemas = [0]*6
opcoes = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']

print("Qual o melhor Sistema Operacional para uso em servidores?")
print("1 - Windows Server \n 2 - Unix \n 3 - Linux \n 4 - Netware \n 5 - Mac OS \n 6 - Outros \n")

#Menu de input dos dados de votação

while True:
   while True:
       opcao = int(input("Digite a opção: "))
       if opcao < 0 or opcao > 6:
           print("Opcao inválida")
       else:
           break
   if opcao == 0:
       break
   sistemas[opcao-1] = sistemas[opcao-1] + 1
   print(sistemas)

#Impressão dos resultados
s
print("Sistema Operacional     Votos    %")
cont = 0
melhor = 0
melhorSistema = ''
perc = 0

for i in sistemas:
    percentual = (i * 100) / sum(sistemas)
    print(f"{opcoes[cont]}, {i}, {percentual}")
    if i > melhor:
        melhor = i
        melhorSistema = opcoes[cont]
        perc = (i * 100) / sum(sistemas)
    cont += 1
print("--------------------------")
print(f"Total {sum(sistemas)}")
print(f"O sistema operacional mais votado foi o {melhorSistema} com {melhor} votos, correspondente a {perc} % dos votos.")