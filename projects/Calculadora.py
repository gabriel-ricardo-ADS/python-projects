history = []

while True:
    op = input("\nOperação (+ - * /) | Histórico (h) | Limpar (c) | Sair (s): ").strip().lower()

    if op == "h":
        if history:
            print("\n Histórico:")
            for item in history:
                print(item)
        else:
            print("Histórico vazio.")
        continue

    if op == "c":
        history.clear()
        print("Histórico apagado.")
        continue

    if op == "s":
        print("Encerrado")
        break

    if op not in ["+", "-", "*", "/"]:
        print("Operação inválida.")
        continue

    num1 = float(input("Digite o primeiro número: ").replace(",", "."))
    num2 = float(input("Digite o segundo número: ").replace(",", "."))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Não divide por zero")
            continue
        result = num1 / num2

    print(f"Resultado: {result}")

    history.append(f"{num1} {op} {num2} = {result}")
