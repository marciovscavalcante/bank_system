menu = """
>>>>>>>> BANCO PYTHON S/A <<<<<<<<

[e] EXTRATO
[d] DEPOSITAR
[s] SACAR
[q] SAIR

Cavalcante Technology©
_______________________
"""

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 5

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Qual valor quer depositar? "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Quanto você quer sacar? "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOps! Tá faltando grana aqui.")

        elif excedeu_limite:
            print("\nOps! Seu limite é menor do que isso.")

        elif excedeu_saques:
            print("\nOps! Sacar tanto parece suspeito. Contate seu gerente.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("\nDeu Ruim! Esse valor aí é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("\nHum, tem algo errado, escolha a opção de novo.")
