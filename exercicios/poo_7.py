'''
Implemente uma classe ContaBancaria.

Atributos:

titular
saldo

Métodos:

depositar(valor)
sacar(valor)
consultarSaldo()

O método sacar() somente deve realizar a operação caso exista saldo suficiente.
'''

class ContaBancaria(): 
    def __init__(self, titular, saldo): 
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor): 
        self.saldo = self.saldo + valor
        print(f'O valor de {valor} foi depositado com sucesso. O saldo atual é {self.saldo}')

    def consultarSaldo(self):
        print(f'O saldo atual é:{self.saldo}')

    def sacar(self, valor): 
        if (self.saldo-valor) >= 0:
            self.saldo = self.saldo - valor
            print(f'O valor de {valor} foi sacado com sucesso!')
        else:
            print("Saldo Insuficiente para realizar o saque!")

conta1 = ContaBancaria("Joao", 1000)
conta1.depositar(500)
conta1.sacar(200)
conta1.consultarSaldo()
