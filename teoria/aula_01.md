# Aula 01 - Definição de conceitos de classe, objeto e atributos # 

---

Primeiramente, para começarmos a compreender os conceitos fundamentais de POO, precisamos entender o que é esse método de programação dentro do Python.

Então, o POO é uma abordagem que eleva a qualidade e a eficiência do código, principalmente quando queremos reaproveita-lo ou deixar ele modular. 

Ou seja, em códigos pequenos, a definição de funções é o suficiente para otimizar um código, mas quando o mesmo fica muito complexo, até mesmo o uso das funções começa a deixa-lo complexo... 

---

## Definição de Classe

Então, vamos iniciar com algumas definições. 

A primeira, que é muito importante, é a definição de Classe. No caso, uma classe em uma linguagem de programação é como um molde para criar objetos. Ela define atributos (características) e métodos (ações) que os objetos criados a partir dela terão. Podemos pensar na classe como se fosse um "molde". 

Por exemplo, uma classe Carro pode ter atributos como “marca” e “modelo” e um método para “exibir_informações”, como mostra o exemplo abaixo: 

```python
class Carro:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo

  def exibir_informacoes(self):
    print(f'Marca: {self.marca}, Modelo: {self.modelo})
```

Ou, se por exemplo, queremos representar alunos em um sistema escolar e verificar se o mesmo foi aprovado ou não em uma disciplina. 

```python
class Aluno:
  def __init__(self, nome, nota):
    self.nome = nome
    self.nota = nota

  def verificar_aprovacao(self):
    if self.nota >= 6:
      return "Aprovado"
    else:
      return "Reprovado"
```

---
## Definição de Objeto

Agora, para criarmos um objeto, instânciamos a classe. No caso, cada objeto terá suas próprias características, mas seguirá o modelo "padrão" da classe, como mostra o exempo abaixo: 

```python
meu_carro = Carro("Toyota", "Corolla")
meu_carro.exibir_informações()
```
