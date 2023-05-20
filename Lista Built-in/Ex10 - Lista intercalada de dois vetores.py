#Faça um Programa que leia dois vetores com 10 elementos cada.
#Gere um terceiro vetor de 20 elementos, cujos valores deverão
#ser compostos pelos elementos intercalados dos dois outros vetores.

A = []
B = []
C = []
for i in range(1,11):
    A.append(i)
for i in range(1,11):
    B.append(i)

for i in range(10):
    C.append(A[i])
    C.append(B[i])

print(f"Os elementos do primeiro vetor são: {A}")
print(f"Os elementos do segundo vetor são: {B}")
print(f"Os elemntos dos dois vetores intercalados: {C}")