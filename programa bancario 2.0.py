import sys

print("*************************")
print("Bem-vindo ao Banco Python")
print("Escolha uma opção abaixo!")
print("*************************")

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Escolha uma opção!
"""

saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Por favor insira o valor do seu deposito: "))
        if deposito <= 0:
            print("Não é possível depositar um valor negativo ou zero.")
        else:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f'Seu depósito de R$ {deposito:.2f} foi realizado com sucesso!')

    elif opcao == "2":
        while numero_saques < LIMITE_SAQUES:
            saque = float(input("Por favor insira o valor que você deseja sacar: "))
            if saque <= 0:
                print("Não é possível sacar um valor negativo ou zero.")
            elif saque > saldo:
                print("Saldo insuficiente para realizar o saque.")
            else:
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                numero_saques += 1
                print(f'Seu saque de R$ {saque:.2f} foi realizado com sucesso!')

            if numero_saques < LIMITE_SAQUES:
                continuar = input("Deseja sacar novamente? (s/n): ").strip().lower()
                if continuar != 's':
                    break
        else:
            print("Limite de saques atingido.")

    elif opcao == "3":
        if saldo > 0:
            print(f"""
            ################# EXTRATO ################# 
            {extrato}
            Seu saldo é de R$ {saldo:.2f}
            #################        ################# 
            """)
        else:
            print("""
            ################# EXTRATO ################# 
            Sem saldo
            #################        ################# 
            """)

    elif opcao == "4":
        print("Saindo... Até mais!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")