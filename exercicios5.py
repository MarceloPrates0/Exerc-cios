import os
os.system("clear")


login_i = input("Insira seu login: ")
senha_i = input("Insira sua senha: ")
repeticao = 0

while True:
    if login_i != senha_i:
        print("Acesso permitido.")
        break
    else:
        print("Acesso negado, insira um login diferente da senha.")
        login_i = input("Insira seu login: ")
        senha_i = input("Insira sua senha: ")
        repeticao += 1
    if repeticao == 2:
        print("Você excedeu o número de tentativas.")
        break

