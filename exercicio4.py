import os
os.system ("clear")

par = 0
impar = 0
negativo = 0
positivo = 0
for i in range(1, 6):
    numero = float(input(f"Insira o {i}º número: "))
    if numero > 0:
        positivo += 1
    else:
        negativo += 1
    
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print()
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativos(s)")
print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
        
        
