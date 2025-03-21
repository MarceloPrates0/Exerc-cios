import os
os.system("clear")

nome = input("Insira seu nome: ")
while True:
    letras = len(nome)
    if letras <= 3:
        print("Quantidade de letras inválida.")
        nome = input("Insira seu nome novamente: ")   
    else:
        print("Nome cadastrado.")
        break

idade = int(input("\nInsira sua idade: "))
while True:
    if idade < 0 or idade > 150:
        print("Idade inválida, insira novamente.")
        idade = int(input("Insira sua idade novamente: "))
    else:
        print("Idade cadastrada.")
        break

salario = float(input("\nInsira seu salário: "))
while True:
    if salario > 0:
        print("Salário aceito.")
        break
    else:
        print("Receba ao menos uma renda para cadastro.")
        salario = float(input("Insira seu salário novamente: "))

genero = input("""
\nInsira seu sexo:
Feminino \t Masculino
F \t \t M
""").upper()
match genero:


    case "M":
        print("Gênero masculino.")
    case "F":
        print("Gênero feminino.")
    case _:
        
        while True:
            if genero != "M" and genero != "F":
                print("Gênero não identificado novamente.")
                genero = input("Insira um gênero válido no sistema: ").upper()
            else:
                print("Gênero computado ")
                break

estado_civil = input("""
Insira seu estado civil:
Casado \t Solteiro\t Viúvo \t Divorciado
C \t S \t\t V \t D                                    
""").upper()
match estado_civil:
    case "C":
        print("Indivíduo casado.")
    case "S":
        print("Individuo solteiro.")
    case "V":
        print("Indivíduo viúvo.")
    case "D":
        print("Indivíduo divorciado.")
    case _:
        while True:
            if estado_civil != "C" and estado_civil != "S" and estado_civil != "V" and estado_civil != "D":
                print("Estado civil inválido no sistema, insira novamente.")
                estado_civil = input("Insira seu estado civil novamente: ").upper()
            else:
                print("Estado civil computado.")
                break
  
