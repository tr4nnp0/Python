"""Vetores estranhos – criei um programa que solicite até 20 números inteiros positivos,
e os armazene em um vetor. A entrada dos números termina ao chegar a 20 ou se o usuário
digitar um valor negativo. Ao termina a entrada de dados imprima os números, a soma dos
números, a quantidade entrada e a média. """

vetor = []
quantidade = 0
soma = 0

while True:
    inteiro =  int(input("Digite um número inteiro: "))
    if inteiro > 0:
        quantidade = quantidade + 1
        soma = inteiro + soma
    if len(vetor) >= 20 or inteiro < 0:
        print("Vetor = ", vetor)
        print("Soma = ", soma)
        print("Quantidade entrada = ", quantidade)
        print("Média = ", soma/quantidade)
        print("Maior = ", max(vetor))
        print("Menor = ", min(vetor))
        break
    vetor.append(inteiro)
    print(vetor)
    
    


        
   
        
            
    
