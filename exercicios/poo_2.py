'''
Crie um programa que utilize esta uma Classe Retangulo. Ele deve pedir ao usuário que informe
a base e altura do retângulo. Depois, deve criar um objeto com as medidas e imprimir a sua
área e o seu perímetro. Para tal, crie uma classe que modele um retângulo:
• Classe: Retangulo
• Atributos: base e altura
• Métodos: calcular ´area, calcular per´ımetro
'''
class Retangulo:
    def __init__(self, base, altura):
        self.altura = altura
        self.base = base

    def calcula_area(self):
        return print(f'A área do retângulo é: {self.base * self.altura}')

    def calcula_perimetro(self):
        return print(f'O perímetro do retângulo é: {2 * (self.base + self.altura)}')

retangulo1 = Retangulo(3,4)
retangulo1.calcula_area()
retangulo1.calcula_perimetro()
