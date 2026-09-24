class SensorTemperatura(): 
    def __init__ (self, identificacao, temperatura):
        self.identificacao = identificacao 
        self.temperatura = temperatura

    def atualizarTemperatura(self, valor): 
        self.temperatura = valor

    def obterTemperatura(self): 
        print(f'A temperatura é de {self.temperatura}')

    def verificarAlarme(self): 
        if self.temperatura > 80: 
            return True 

        else: 
            return False 
