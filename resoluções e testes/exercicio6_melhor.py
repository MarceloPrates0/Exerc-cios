import os
os.system("clear")

# Nome
nome = input("Insira seu nome: ")
while len(nome) <= 3:
    print("Quantidade de letras inválida.")
    nome = input("Insira seu nome novamente: ")   
print("Nome cadastrado.")

# Idade
idade = int(input("\nInsira sua idade: "))
while idade < 0 or idade > 150:
    print("Idade inválida, insira novamente.")
    idade = int(input("Insira sua idade novamente: "))
print("Idade cadastrada.")

# Salário
salario = float(input("\nInsira seu salário: "))
while salario <= 0:
    print("Receba ao menos uma renda para cadastro.")
    salario = float(input("Insira seu salário novamente: "))
print("Salário aceito.")

# Gênero
genero = input("""
\nInsira seu sexo:
Feminino \t Masculino
F \t \t M
""").upper()
while genero not in ['M', 'F']:
    print("Gênero não identificado, insira novamente.")
    genero = input("Insira um gênero válido no sistema: ").upper()

match genero:
    case "M":
        print("Gênero masculino.")
    case "F":
        print("Gênero feminino.")

# Estado civil
estado_civil = input("""
Insira seu estado civil:
Casado \t Solteiro\t Viúvo \t Divorciado
C \t S \t\t V \t D                                    
""").upper()
while estado_civil not in ['C', 'S', 'V', 'D']:
    print("Estado civil inválido no sistema, insira novamente.")
    estado_civil = input("Insira seu estado civil novamente: ").upper()

match estado_civil:
    case "C":
        print("Indivíduo casado.")
    case "S":
        print("Indivíduo solteiro.")
    case "V":
        print("Indivíduo viúvo.")
    case "D":
        print("Indivíduo divorciado.")