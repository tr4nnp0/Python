#Faça um programa que leia a média de alunos de uma determinada turma,
#encontre e exiba o maior valor de média inserida. Obs.: Não há informação
#prévia sobre a quantidade de alunos da turma

media = input("Digite o valor da média do aluno: ")
maior_valor = 0

while True:
    if media == "fim":
        break
    try:
        imedia = int(media)
    except:
        print("Digite um valor inteiro")

    if imedia > maior_valor:
        maior_valor = imedia
    media = input("Digite o valor da média do aluno: ")

print("O valor da maior média inserida é: ", maior_valor)
    
