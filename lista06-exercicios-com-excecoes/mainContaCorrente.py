from contaCorrente import ContaCorrente
import time

conta1 = ContaCorrente(1234,"João",953)
conta2 = ContaCorrente(1235,"Maria",1000)
conta3 = ContaCorrente(1236,"José",500)
conta4 = ContaCorrente(1237,"Ana",100)
conta5 = ContaCorrente(1238,"Pedro")
conta6 = ContaCorrente(1239,"Paulo")
conta7 = ContaCorrente(1240,"Carlos")
conta8 = ContaCorrente(1241,"Lucas",450)
conta9 = ContaCorrente(1242,"Marcos",15000)
conta10 = ContaCorrente(1243,"Júlia",100000)

contas = [conta1,conta2,conta3,conta4,conta5,conta6,conta7,conta8,conta9,conta10]

while True:
    time.sleep(0.5)
    print('')
    print('===============================')
    print('====== BANCO DO PYTHON ========')
    print('===============================')
    print('(d) depositar')
    print('(s) sacar')
    print('(v) ver saldo')
    print('(t) terminar')
    print('===============================')

    opcao = input('Opção: ')

    if opcao == 'd':
        numero = int(input('Número da conta: '))
        valor = float(input('Valor: '))
        for conta in contas:
            if conta.numero == numero:
                conta.depositar(valor)
                print('Depósito realizado com sucesso!')
                break
        else:
            print('Conta não encontrada!')
    
    elif opcao == 's':
        numero = int(input('Número da conta: '))
        valor = float(input('Valor: '))
        for conta in contas:
            if conta.numero == numero:
                if conta.sacar(valor):
                    print('Saque realizado com sucesso!')
                else:
                    print('Saldo insuficiente!')
                break
        else:
            print('Conta não encontrada!')

    elif opcao =='v':
        numero = int(input('Número da conta: '))
        for conta in contas:
            if conta.numero == numero:
                print(conta.saldo)
                break
        else:
            print('Conta não encontrada.')

    elif opcao == 't':
        print('Sua operação foi finalizada.')
        break

    else:
        print('Caractere inválido.')

