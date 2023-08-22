class ContaCorrente:

    def __init__(self):
        self.numero = ""
        self.__saldo = 0.0

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            raise Exception("Valor inválido")