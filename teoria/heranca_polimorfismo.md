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

## Polimorfismo ## 

## Abstração ## 
