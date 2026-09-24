class Produto: 
    def __init__ (self, nome, preco): 
        self.nome = nome 
        self.__preco = preco

    def get_preco(self): 
        return self.__preco 

    def set_preco(self, novo_preco): 
        if novo_preco > 0: 
            self.__preco = novo_preco
            return self.__preco
        else: 
            return self.__preco 

produto = Produto("Teclado", 150)

produto.set_preco(200)
print(produto.get_preco())

produto.set_preco(-50)
print(produto.get_preco())
