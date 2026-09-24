''' Exercício 1 - POO
Crie um programa que utilize esta uma Classe Triangulo. Ele deve pedir ao usuário que informe
as medidas de um triangulo. Depois, deve criar um objeto com as medidas e imprimir sua área
e maior lado. Para tal, crie uma classe que modele um triangulo:
• Classe: Triangulo
• Atributos: LadoA, LadoB e LadoC
• Métodos: calcular Perímetro e retornar o maior lado (getMaiorLado)
'''

class Triangulo: 
    def __init__(self, LadoA, LadoB, LadoC):
        self.LadoA = LadoA
        self.LadoB = LadoB
        self.LadoC = LadoC

    def calcular_perimetro(self):
        per = self.LadoA +  self.LadoB + self.LadoC
        return (f'O perímetro do triângulo é: {per}')

    def getMaiorLado(self):
        lados = [self.LadoA, self.LadoB, self.LadoC]
        maior_lado = max(lados)
        posicao = lados.index(maior_lado)
        return print(f'O maior lado é: {lados[posicao]}')

triangulo1 = Triangulo(3,4,5)
print(triangulo1.calcular_perimetro())
triangulo1.getMaiorLado()
