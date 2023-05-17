""" Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
  O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
 Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""

class Televisor:
    def __init__(self, canal: int, volume: int ):
        self.canal = canal
        self.volume = volume

    def Aumentar_volume(self, acréscimo):
        self.volume += acréscimo

    def Diminuir_volume(self, decréscimo):
        self.volume -= decréscimo

    def Faixa_canal(self):
        if 0 < self.canal < 100:
            print("Canal dentro de frequência válida")
        else:
            print("Canal fora de frequência válida")

    def Nível_volume(self):
        if 0 < self.volume < 50:
            print("Volume dentro dos limites de ruído")
        else:
            print("Volume fora dos limites de ruído")

    def Mostrar_Dados(self):
        print(f"Canal: {self.canal}, Volume: {self.volume}")

Televisor1 = Televisor(38, 56)
Televisor1.Aumentar_volume(25)
Televisor1.Diminuir_volume(0)
Televisor1.Faixa_canal()
Televisor1.Nível_volume()
Televisor1.Mostrar_Dados()