'''
Implemente uma classe chamada Carro com as seguintes propriedades:
• Um ve´ıculo tem um certo consumo de combust´ıvel (medidos em km/litro) e uma certa
quantidade de combust´ıvel no tanque
• O consumo ´e especificado no construtor e o n´ıvel de combust´ıvel inicial ´e 0
• Forne¸ca um m´etodo andar( ) que simule o ato de dirigir o ve´ıculo por uma certa distˆancia, reduzindo o n´ıvel de combust´ıvel no tanque de gasolina. Esse m´etodo recebe como parˆametro
a distˆancia em km
• Forne¸ca um m´etodo obterGasolina( ), que retorna o n´ıvel atual de combust´ıvel
• Forne¸ca um m´etodo adicionarGasolina( ), para abastecer o tanque
'''

class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.tanque = 0

    def andar(self, distancia):
        litros_gastos = distancia / self.consumo
        self.tanque = self.tanque - litros_gastos
        return

    def adicionarGasolina(self, quantidade):
        self.quantidade = quantidade
        self.tanque = self.tanque + quantidade

    def obterGasolina(self):
        return print(f'O atual nível de combustível é: {self.tanque} litros')

meuFusca = Carro (15) ; #15 quilometros por litro de combustivel
meuFusca.adicionarGasolina (20) ; # abastece com 20 litros de combustivel
meuFusca.andar (100) ; # anda 100 quilometros
meuFusca.obterGasolina() # Imprime o combustivel que resta no tanque
