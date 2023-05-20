"""Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro
de combustível. Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e
quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição
das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout."""

#Declaração dos valores

modelos = ['fusca', 'gol', 'uno', 'vectra', 'peugeot']
kmporlitro = [7, 10, 12.5, 9, 14.5]

print("Comparativo de Consumo de Combustível")

#Impressão dos dados iniciais

for i in range(len(modelos)):
    print(f"Veículo {i+1}")
    print(f"Nome: {modelos[i]}")
    print(f"Km por litro: {kmporlitro[i]}\n")

#Calculo do consumo por km por automóvel

custopor1000 = []
consumoporcarro = []
for i in range(len(modelos)):
    custo = (kmporlitro[i]*1000)/2.25
    consumo = 1000/kmporlitro[i]
    custopor1000.append(custo)
    consumoporcarro.append(consumo)

print("Relatório Final")

#Impressão dos resultados de consumo por automóvel e menor consumo

menor_consumo = []
consumo_minimo = 0
for i in range(len(kmporlitro)):
    litros = 1000/kmporlitro[i]
    print(f"{i+1} - {modelos[i]}           - {kmporlitro[i]:.1f} -  {consumoporcarro[i]:.1f} litros -  R$ {custopor1000[i]:.1f}")


print(f"O menor consumo é o: {(modelos[consumoporcarro.index(min(consumoporcarro))])}")