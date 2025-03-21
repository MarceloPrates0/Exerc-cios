import os
os.system ("clear")

nome = input("Insira seu nome: ")
texto = len(nome)
if texto <= 3:
    print("Bloqueado")
else:
    print("Permitido")