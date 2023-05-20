#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da
#pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

cont = 0
Respostas = []
while True:
    Pergunta1 = input("Telefonou para a vítima?\n")
    Pergunta2 = input("Esteve no local do crime?\n")
    Pergunta3 = input("Mora perto da vítima?\n")
    Pergunta4 = input("Devia para a vítima?\n")
    Pergunta5 = input("Já trabalhou para a vítima?\n")

    Respostas.append(Pergunta1)
    Respostas.append(Pergunta2.append(Pergunta3))
    Respostas
    Respostas.append(Pergunta4)
    Respostas.append(Pergunta5)
    print(Respostas)

    for i in range(len(Respostas)):
        if Respostas[i] == "s" or Respostas[i] == "sim" or Respostas[i] == "SIM" or Respostas[i] == "Sim":
            cont = cont + 1
        print(cont)

    if cont <= 2:
        print("A pessoa é inocente!")
    if 3 <= cont <= 4:
        print("A pessoa é suspeita!")
    if cont == 5:
        print("A pessoa é assassina!")

    Pergunta6 = input("Quer refazer o questionário?")
    if Pergunta6 == "Não" or Pergunta6 == "N" or Pergunta6 == "NÃO" or Pergunta6 == "não":
        break




