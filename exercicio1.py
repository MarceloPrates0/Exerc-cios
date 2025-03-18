import os
os.system ("clear")

input("Insira seu nome: ")
salario = float(input("Insira seu salário fixo: R$"))
vendas = float(input("Insira sua quantidade de vendas em dinheiro: R$"))

total_venda = vendas * 0.15
total_liquido = salario + total_venda

print(f"\nSeu total valor total de comissão esse mês foi: R${total_venda:.2f}")
print(f"Seu total neste mês foi de: R${total_liquido:.2f}")




