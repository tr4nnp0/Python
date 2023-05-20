#Uma agência de uma cidade do interior tem, no máximo, 10.000 clientes.
#Faça um programa que leia o número da conta e o saldo de cada cliente.
#A leitura de clientes termina quando for digitado -999 para número da conta
#ou quando atingir 10.000 clientes. O programa deve calcular e imprimir o total
#de clientes com saldo negativo, o total de clientes da agência e o saldo da agência.

total_clientes = 0
saldo_clientes_negativo = 0
saldo_agência = 0

while True:
    conta = int(input("Digite o número da conta: "))
    total_clientes = total_clientes + 1
    if conta == -999 or total_clientes > 10000 :
        break
    saldo = int(input("Digite o saldo da conta: "))
    saldo_agência = saldo_agência +  saldo
    if saldo < 0:
        saldo_clientes_negativo = saldo_clientes_negativo + 1

print("O total de clientes com saldo negativo é: ", saldo_clientes_negativo)
print("O total de clientes da agência é: ", saldo_clientes_negativo)
print("O saldo total da agência é: ", saldo_agência)

    
        
    
