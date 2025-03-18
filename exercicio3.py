import os
os.system ("clear")

impar = 0
par = 0
soma = 0

for i in range(1, 7):
    numero = float(input("Insira um número: "))
    if numero > 0:
        soma += numero
    if numero < 0:
        impar += 1
    else:
        par += 1

media = soma / par

print(f"Você pôs {par} numeros pares")
print(f"Sua média é de {media}")