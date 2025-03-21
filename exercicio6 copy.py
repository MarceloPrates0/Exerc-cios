import os
os.system("clear")

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

               

