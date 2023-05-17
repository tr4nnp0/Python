""" Implemente uma classe Carro com as seguintes propriedades:
  - Um veículo tem um certo consumo de combustível(medidos em Km / litro)
  e uma certa quantidade de combustível no tanque
  - O consumo é especificado no construtor e o nível inicial do combustivél é zero
  - Forneça um método mover (km) que receba a distância em quilômetros e reduza o nivel de
  combustível no tanque de gasolina.
  - Forneça um método gasolina que retorno o nivel atual de combustível.
  - Forneça um método abastecer(litros), para abastecer o tanque."""

class Carro:
    def __init__(self, consumo, quantidadeCombustivel):
        self.consumo = consumo
        self.quantidadeCombustivel = quantidadeCombustivel

    def andar(self, distancia):
        self.quantidadeCombustivel -= (distancia/self.consumo)

    def obterGasolina(self):
        print(f"A quantidade de combustível depois de percorrido o trecho definido é: {self.quantidadeCombustivel} litros")

    def adicionarGasolina(self, abastecimento):
        self.quantidadeCombustivel += abastecimento
        print(f"A quantidade de combustível após o abastecimento é: {self.quantidadeCombustivel} litros")


meuFusca = Carro(12,20)
meuFusca.andar(100)
meuFusca.obterGasolina()
meuFusca.adicionarGasolina(10)
