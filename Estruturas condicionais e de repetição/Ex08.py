"""Faça um programa em Python que leia uma senha aleatória e forneça seu tamanho, e
imprima uma versão maiúscula e uma minúscula da senha.
exemplo de saída: (senha:”AbCd123”)
tamanho da senha: 7
versão maiúscula: ABCD123
versão minúscula: abcd123

(opcional) – incremente o programa e valide uma senha segundo os seguintes critérios:
•	Tamanho – de 6 a 8 caracteres;
•	Pelo menos 1 número;
•	Não pode começar por número;
•	Pelo menos 1 letra maiúscula; """

print("Para que sua senha seja válida, deve obedecer a quatro critérios: \n(1) - Estar entre 6-8 caracteres;\n(2) - Ter pelo menos 1 número;\n(3) - Não pode começar com um número;\n(4) - E ter pelo menos 1 letra maiúscula")
senha = input("Digite uma senha válida: ")
senha_lista = list(senha)

num_caractere = 0
num_digito = 0
primeiro_digito = 0
num_maiúscula = 0

for elemento in senha_lista:
    if elemento.isalpha() == True:
        num_caractere = num_caractere + 1
    if elemento.isdigit() == True:
        num_digito = num_digito + 1
    if elemento.isupper():
        num_maiúscula = num_maiúscula + 1

maiúsculo = senha.upper()
minúsculo = senha.lower()
print("A sua senha tem %d caracteres" %(len(senha)))
print("versão maiúscula: ", maiúsculo)
print("versão minúscula: ", minúsculo)
print("Sua senha tem %d números" %(num_digito))

primeiro_digito = senha_lista[0]
print(primeiro_digito)

if senha_lista[0].isdigit() == True:
    print("Sua senha começa com um número!")
else:
    print("Sua senha não começa com um número!")
    
print("Sua senha tem %d letra(s) maiúscula(s)" %(num_maiúscula))
        
if 6<=len(senha)<=8 and num_digito > 0 and senha_lista[0].isdigit() == False and num_maiúscula > 0:
    print("Sua senha está dentro dos parâmetros de segurança!")
else:
    print("Sua senha está fora dos parâmetros de segurança!")
        
