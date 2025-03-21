def ao_clicar():
    print("Você clicou no botão!")

# Simulando um botão com entrada de texto
while True:
    acao = input("Digite 'clicar' para acionar o botão ou 'sair' para encerrar: ").strip().lower()

    if acao == "clicar":
        ao_clicar()
    elif acao == "sair":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")