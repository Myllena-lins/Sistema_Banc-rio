# Sistema Bancário
print("Bem vindo ao Banco Myllena!".center(50))
print("="*50)

print("\nEscolha uma das opções do menu disponível para os nossos clientes:")

menu = """

[D/d] Depositar
[S/s] Sacar
[E/e] Extrato
[C/c] Consultar Saldo da Conta
[Q/q] Sair

=> """

saldo = 0
limite_saque_diario = 500
extrato = ""
numero_saque = 0
saque_maximo = 3

while True:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação inválida! Informe um valor positivo para o depósito!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if valor > 0:
            if valor <= saldo:
                if valor <= limite_saque_diario:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    numero_saque += 1
                    print("Saque realizado com sucesso!")
                    if numero_saque >= saque_maximo:
                        print("Limite de saques diários atingido!")
                else:
                    print("Você ultrapassou o limite de saque diário!")
            else:
                print("Saldo insuficiente!")
        else:
            print("Operação inválida! Informe um valor positivo para o saque!")

    elif opcao == "e":
        print("Extrato:".center(50))
        print("="*50)
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "c":
        print("Saldo da Conta:".center(50))
        print("="*50)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços! Volte sempre!")

    else:
        print("Opção inválida! Escolha uma opção do menu.")
