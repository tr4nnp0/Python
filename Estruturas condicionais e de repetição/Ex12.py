"""5.	Frases malucas - Em algumas situações é preciso gerar textos aleatórios para teste
(por exemplo para preencher o design de um site em construção) Para este fim, escreva um
programa que gere 5 textos aleatórios baseado nas listas de palavras abaixo:
artigos = ["o", "a", "um", "uma"]
sujeitos = ["gato", "cachorro", "homem", "mulher"]
verbos = ["cantar", "correr", "pular", "nadar"]
adverbios = ["vagarosamente", "silenciosamente", "bem", "mal"]
"""

import random

artigos = ["o", "a", "um", "uma"]
sujeitos = ["gato", "cachorro", "homem", "mulher"]
verbos = ["cantar", "correr", "pular", "nadar"]
adverbios = ["vagarosamente", "silenciosamente", "bem", "mal"]

texto_1 = random.choice(artigos)
texto_2 = random.choice(sujeitos)
texto_3 = random.choice(verbos)
texto_4 = random.choice(adverbios)

print(texto_1, texto_2, texto_3, texto_4)
print(texto_1, texto_2, texto_3)

estrutura_1 = (texto_1, texto_2, texto_3, texto_4)
estrutura_2 = (texto_1, texto_2, texto_3)

opção = random.randint(1,2)
print("Escolha aleatória: estrutura", opção)

if opção == 1:
    print(*estrutura_1)
else:
    print(*estrutura_2)
