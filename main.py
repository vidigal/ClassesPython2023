from cliente import Cliente
from conta_corrente import ContaCorrente

conta1 = ContaCorrente()
conta1.saldo = 100000.0
conta1.numero = "07355454-44"

conta2 = ContaCorrente()
conta2.saldo = 1000000000.0
conta2.numero = "12325253-44"


cliente = Cliente()
cliente.nome = "João"
cliente.cpf = "456.654.654-55"

#Adicionando uma conta na lista de contas do objeto cliente
cliente.contas.append(conta1)
cliente.contas.append(conta2)

for conta in cliente.contas:
    print(f"Saldo da conta {conta.numero} é {conta.saldo}")