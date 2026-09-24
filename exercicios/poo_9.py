'''
Crie uma classe Motor.

Atributos:

potencia
ligado
temperatura

O motor deve iniciar desligado e com temperatura de 25 °C.

Métodos:

ligar()
desligar()
aquecer(valor)
obterTemperatura()

O método aquecer() só deve aumentar a temperatura caso o motor esteja ligado.
'''

class Motor: 

    def __init__ (self, potencia): 
        self.potencia = potencia
        self.ligado = False
        self.temperatura = 25

    def ligar(self): 
        self.ligado = True
        print(f'O motor foi ligado!')

    def desligar(self): 
        self.ligado = False
        print('O motor foi desligado!')

    def aquecer(self, valor): 
        if self.ligado == True: 
            self.temperatura = self.temperatura + valor
            print(f'O motor foi aquecido e agora está com uma temperatura de {self.temperatura}')

        else:
            print('O motor não está ligado, logo, não pode ser aquecido!')

    def obterTemperatura(self): 
        print(f'O motor está à uma temperatura de: {self.temperatura} graus.')

m1 = Motor(100)
m1.aquecer(20)
m1.ligar()
m1.aquecer(30)
m1.desligar()
m1.aquecer(10)
m1.obterTemperatura()
