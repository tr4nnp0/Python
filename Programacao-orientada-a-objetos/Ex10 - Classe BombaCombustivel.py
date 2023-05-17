"""Faça um programa completo utilizando classes e métodos que:
A - Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel;
valorLitro;
quantidadeCombustivel.
B - Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo;
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente;
alterarValor( ) – altera o valor do litro do combustível;
alterarCombustivel( ) – altera o tipo do combustível;
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba."""

class bombaCombustivel:
    def __init__(self, tipoCombustivel = 'gasolina', valorLitro = 5.54, quantidadeDeCombustivel = 10):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeDeCombustivel = quantidadeDeCombustivel

    def abastecerPorValor(self):
        print(f"O valor do litro é: {self.valorLitro} reais")
        print(f"O valor abastecido é: {self.quantidadeDeCombustivel} litros")

    def abastecerPorLitro(self):
        print(f"A quantidade em litros de combustível é: {self.quantidadeDeCombustivel} litros")
        print(f"O valor a ser pago pelo cliente é: {self.valorLitro*self.quantidadeDeCombustivel} reais")

    def alterarValor(self, valorLitro):
        self.valorLitro = valorLitro
        print(f"O novo valor do combustível é: {valorLitro} reais")

    def alterarCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel
        print(f"O novo tipo de combustível escolhido é: {tipoCombustivel}")

    def alterarQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel
        print(f"A nova quantidade de combustível é: {quantidadeCombustivel} litros")

cliente = bombaCombustivel()
cliente.abastecerPorValor()
cliente.abastecerPorLitro()
cliente.alterarValor(6)
cliente.alterarCombustivel("Etanol")
cliente.alterarQuantidadeCombustivel(20)