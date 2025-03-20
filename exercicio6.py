# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

import os
os.system ("clear")

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
salario = float (input("Insira seu salário: "))
genero = input("""
Insira seu sexo:
Masculino \t Feminino
M \t \t F
""")
estado_c = input("""
Insira seu estado civil: 
c - Casado
s - Solteiro
v - Viúvo                        
d - Divorciado                               
""")
