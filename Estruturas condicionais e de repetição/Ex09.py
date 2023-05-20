"""Rescreva o programa do exercício anterior, criando e utilizando as seguintes funções:
•	tamanhovalido(s, tamanho) – retorna “true” se o tamanho da string “s” é menor ou igual ao número “tamanho”; caso contrário “false”
•	senhamaiuscula(s) – retorna a versão maiúscula de s
•	senhaminuscula(s) - retorna a versão minúscula de s
"""

print("O programa a seguir permite avaliar os seguintes critérios de sua senha:\n(1) Se ela está ou não dentro dos critérios\n(2) Visualizar suas versões maíuscula e minúscula\n(3)Se tem pelo menos 1 número;\n(4) Se começa ou não com um número;\n(5) Se tem pelo menos 1 letra maiúscula\n")
s = input("Insira sua senha para receber a avaliação: ")
tamanho = len(s)
s_lista = list(s)

def tamanhovalido(s, tamanho):
    if 6<=tamanho<=8:
        print("Tem entre 6 e 8 caracteres? Resposta: ", True)
    else:
        print("Tem entre 6 e 8 caracteres? Resposta: ", False)

def senhamaiúscula(s):
    maiúscula = s.upper()
    print(maiúscula)

def senhaminúscula(s):
    minúscula = s.lower()
    print(minúscula)

def valida1dig(s):
    num_digito = 0
    for elemento in s_lista:
        if elemento.isalpha() == True:
            num_digito = num_digito + 1
    if num_digito > 0:
        print("A senha tem ao menos 1 número? Resposta: ", True)
    else:
        print("A senha tem ao menos 1 número? Resposta: ", False)

def no1number(s):
    if s_lista[0].isdigit() == True:
        print("O primeiro dígito da senha é numérico? Resposta: ", True)
    else:
         print("O primeiro dígito da senha é numérico? Resposta: ", False)


def pelomenos1maiusc(s):
    num_maiúscula = 0
    for elemento in s_lista:
        if elemento.isupper() == True:
            num_maiúscula = num_maiúscula + 1
    if num_maiúscula > 0:
        print("A senha tem ao menos 1 letra maiúscula? Resposta: ", True)
    else:
        print("A senha tem ao menos 1 letra maiúscula? Resposta: ", False)


tamanhovalido(s, tamanho)
senhamaiúscula(s)
senhaminúscula(s)
valida1dig(s)
no1number(s)
pelomenos1maiusc(s)
