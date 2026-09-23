'''
Implemente uma classe Funcionário que tem: (i) um construtor com dois parâmetros (nome e
salário) e (ii) um método aumentarSalario que aumenta o salário do funcionário em uma certa
porcentagem. 
'''

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual):
        print(f'O salário atual de {self.nome} é: {self.salario}')
        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        print(f'O novo salário de {self.nome} é: {self.salario}')

funcionario1 = Funcionario("João", 3000)
funcionario1.aumentar_salario(10)
