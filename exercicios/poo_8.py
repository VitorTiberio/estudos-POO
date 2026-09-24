'''
Crie uma classe Bateria.

Atributos:

capacidade
cargaAtual

Ao criar uma bateria, sua carga inicial deve ser 0.

Métodos:

carregar(quantidade)
Aumenta a carga da bateria, sem permitir que ultrapasse sua capacidade.

consumir(quantidade)
Reduz a carga, desde que exista carga suficiente.

obterCarga()
Retorna a carga atual.
'''

class Bateria(): 
    def __init__(self, capacidade): 
        self.capacidade = capacidade
        self.cargaAtual = 0

    def carregar(self, quantidade): 
        if (self.cargaAtual + quantidade) <= self.capacidade:
            self.cargaAtual = self.cargaAtual + quantidade
            print(f'A bateria foi carregada com sucesso! A carga atual é: {self.cargaAtual}')    
        else: 
            print(f'Nao foi possível completar a carga, já que ultrapassa o limite de carregamento.')
        

    def consumir(self, quantidade): 
        if self.cargaAtual >= quantidade: 
            self.cargaAtual = self.cargaAtual - quantidade
        else: 
            print('A bateria não está com carga suficinete para ser consumida por essa quantidade.')

    def obterCarga(self): 
        print(f'A carga atual é de: {self.cargaAtual}')

b1 = Bateria(5000)

b1.carregar(3000)
b1.consumir(800)
b1.carregar(4000)
b1.obterCarga()
