def menu():
    menu = """\n
    >>>>>>>> BANCO PYTHON S/A <<<<<<<<

    [d]  DEPOSITAR
    [s]  SACAR
    [e]  EXTRATO
    [nc] NOVA CONTA
    [lc] LISTAR CONTAS
    [nu] NOVO USUÁRIO
    [q]  SAIR

    Cavalcante Technology©
    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito\tR$ {valor:.2f}\n"
        print("\n Depósito feito")
    else:
        print("\n Ops! Deu ruim, valor inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

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
        print("\nSaque Feito!")

    else:
        print("\nDeu Ruim! Esse valor aí é inválido.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Diga qual o CPF (Somente os números, ok?): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nOps! Alguém já usa esse CPF!")
        return
    
    nome = input("Qual o nome do usuário? ")
    data_nascimento = input("Qual a data de nascimento (dd/mm/aaaa)? ")
    endereco = input("Qual o endereço? ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuário adicionado!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Diga qual o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado, conta não criada.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            Conta Corrente:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 5
    AGENCIA = "0001"
    
    saldo = 0
    limite = 1000
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Qual valor quer depositar? "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Quanto você quer sacar? "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if  conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\nHum, tem algo errado, escolha a opção de novo.")

main()