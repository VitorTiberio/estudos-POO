## Encapsulamento ## 

Consiste em agrupar dados e comportamentos dentro de uma classe e controla a maneira de como esses dados são acessados ou modificados. 

Por exemplo, imagine uma conta bancária, não seria interessante permitir: 

```python
conta.saldo = -1000000
```

A ideia é que a própria classe determine como o saldo pode ser alterado. Um exemplo pode ser consultado abaixo: 

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def consultar_saldo(self):
        return self.__saldo
```

Para testar a implementação, podemos usar: 

```python
conta = ContaBancaria("Vitor", 1000)
conta.depositar(500)
print(conta.consultar_saldo())
```

Observe que na classe __init__, existe um atributo chamado self.__saldo. Em python, isso ativa o chamado *name mangling*, dificultando o acesso ao atributo. 

No caso, a ideia é que o usuário da classe utilize: 
```python
conta.depositar(500)
conta.consultar_saldo()
```
Ao invés de manipular diretamente o saldo. 

---

## Herança ## 

A herança permite criar uma classe nova a partir de uma classe existente. No caso, pense no caso de termos duas classes: Professor e Aluno. Ambos possuem características como nome, idade e CPF. Ao invés de recetir tudo, podemos criar uma classe geral: 

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Meu nome é {self.nome}")
```
Agora, podemos fazer: 
```python
class Aluno(Pessoa):
    def estudar(self):
        print("Estou estudando.")
```

A sintaxe: 
```python
class Aluno(Pessoa):
```
Significa que o Aluno herda de pessoa. Assim, podemos escrever: 

```python
aluno = Aluno("Vitor", 22)
print(aluno.nome)
aluno.apresentar()
aluno.estudar()
```
Embora Aluno não tenha declarado nome nem apresentar(), ele herdou esses elementos de Pessoa. 

Agora, suponha que Aluno tenha também um número de matrícula: 
```python
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
```

A parte: super().__init__(nome,idade) chama o construtor da classe pai. Ou seja, é a mesma coisa que falar: "inicialize para mim a parte referente a nome e idade". 

---

## Polimorfismo ## 

## Abstração ## 
