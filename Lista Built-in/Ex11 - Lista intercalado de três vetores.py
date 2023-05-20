#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

A = []
B = []
C = []
D = []
for i in range(1,11):
    A.append(i)
for i in range(1,11):
    B.append(i)
for i in range(1,11):
    C.append(i)

for i in range(10):
    D.append(A[i])
    D.append(B[i])
    D.append(C[i])

print(f"Os elementos do primeiro vetor são: {A}")
print(f"Os elementos do segundo vetor são: {B}")
print(f"Os elementos do terceiro vetor são: {C}")
print(f"Os elemntos dos três vetores intercalados: {D}")