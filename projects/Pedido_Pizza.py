## PEDIDO PIZZA 

dict_cardapio = {
    "3 Queijos": 30,
    "4 Queijos": 35,
    "Portuguesa": 42,
    "Calabresa": 37,
    "Bacon": 40,
    "Italiana": 33
}

pedido = []

def lista_cardapio():
    print("\n===== CARDÁPIO =====")
    for sabor, valor in dict_cardapio.items():
        print(f"{sabor:<12} R$ {valor}")              #<12 reserva 12 espaços a esquerda
    print()

def mostrar_contato():
    print("""
===== CONTATO =====
 Telefone: (11) 99999-9999
 Endereço: Rua Mandaqui, 33 - São Paulo
 Email: contato@zepizzas.com
""")

while True:
    try:
        opcao = int(input("""
Olá! Bem vindo ao Zé Pizzas 
1 - Ver cardápio
2 - Fazer pedido
3 - Ver pedido
4 - Fale conosco!
5 - Sair
Escolha: """))
    except ValueError:
        print("Digite apenas números.")
        continue

    if opcao == 1:
        lista_cardapio()

    elif opcao == 2:
        tipo = input("Pizza normal ou meio a meio? (n/m): ").lower()

        if tipo == "n":
            sabor = input("Digite o sabor desejado: ")
            if sabor in dict_cardapio:
                pedido.append((sabor, dict_cardapio[sabor]))
                print("Pizza adicionada!\n")
            else:
                print("Sabor não encontrado.\n")

        elif tipo == "m":
            sabor1 = input("Digite o primeiro sabor: ")
            sabor2 = input("Digite o segundo sabor: ")

            if sabor1 in dict_cardapio and sabor2 in dict_cardapio:
                valor = (dict_cardapio[sabor1] + dict_cardapio[sabor2]) / 2
                nome = f"Meio a meio: {sabor1} / {sabor2}"
                pedido.append((nome, valor))
                print("Pizza meio a meio adicionada!\n")
            else:
                print("Um dos sabores não foi encontrado.\n")
        else:
            print("Opção inválida.\n")

    elif opcao == 3:
        if not pedido:
            print("Você ainda não fez nenhum pedido.\n")
        else:
            total = 0
            print("\n===== SEU PEDIDO =====")
            for nome, valor in pedido:
                print(f"{nome:<35} R$ {valor}")
                total += valor
            print(f"\nTOTAL: R$ {total}\n")

    elif opcao == 4:
        mostrar_contato()

    elif opcao == 5:
        print("Obrigado por escolher o Zé Pizzas!")
        break

    else:
        print("Opção inválida.\n")