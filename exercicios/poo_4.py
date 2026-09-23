'''
Implemente uma classe Aluno, que deve ter os seguintes atributos: nome, curso, tempoSemDormir (em horas). Essa classe dever´a ter os seguintes m´etodos:
• Estudar (que recebe como parˆametro a quantidade de horas de estudo e acrescenta tempoSemDormir)
• Dormir (que recebe como parˆametro a quantidade de horas de sono e reduz tempoSemDormir)
'''

class Aluno:
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    def estudar(self, horas):
        print(f'O aluno {self.nome} está estudando por {horas} horas.')
        self.tempoSemDormir += horas
        print(f'Tempo sem dormir do aluno {self.nome} agora é: {self.tempoSemDormir} horas.')

    def dormir(self, horas_sono):
        print(f'O aluno {self.nome} está dormindo por {horas_sono} horas.')
        self.tempoSemDormir -= horas_sono
        if self.tempoSemDormir < 0:
            self.tempoSemDormir = 0
        print(f'Tempo sem dormir do aluno {self.nome} agora é: {self.tempoSemDormir} horas.')

aluno1 = Aluno("Maria", "Engenharia", 5)
aluno1.estudar(3)
aluno1.dormir(4)
