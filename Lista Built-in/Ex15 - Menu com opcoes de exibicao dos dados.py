#Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
#encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
#Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;

lista = []
acima_media = []
acima_sete = []

while True:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    if numero == -1:
        lista.remove(-1)
        break

print(f"O número de elementos da lista é: {len(lista)}")
print(f"A lista dos valores informados é: {lista}")

lista_inversa = lista[::-1]
for i in range(len(lista_inversa)):
    print(f"{lista_inversa[i]}\n")

media = sum(lista)/len(lista)

print(f"A soma dos valores da lista é: {sum(lista)}")
print(f"A média dos valores da lista é: {media}")

for i in range(len(lista)):
    if lista[i] > media:
        acima_media.append(lista[i])

print(f"Os valores acima da média são: {acima_media}")

for i in range(len(lista)):
    if lista[i] > 7:
        acima_sete.append(lista[i])

print(f"Os valores acima de sete são: {acima_sete}")
print(f"Tenha uma boa noite!")