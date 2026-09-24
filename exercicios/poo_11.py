class ContaBancaria: 
    def __init__ (self, titular, saldo): 
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor): 
        if valor > 0: 
            self.__saldo = self.__saldo + valor

    def sacar(self, valor): 
        if self.__saldo > valor: 
            self.__saldo = self.__saldo - valor

    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria("João", 1000)
conta.depositar(500)
conta.sacar(200)

print(conta.consultar_saldo())
