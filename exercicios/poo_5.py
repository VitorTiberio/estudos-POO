'''
Crie um programa que utilize as classes Loja e Produto para simular um sistema de vendas
simples. O programa deve permitir ao usu´ario realizar as seguintes opera¸c˜oes: (i) adicionar um
produto `a loja (ii) realizar uma venda de um produto e (iii) exibir as informa¸c˜oes de todos os
produtos da loja. Lembre-se de utilizar os m´etodos das classes Loja e Produto para realizar as
opera¸c˜oes necess´arias. Para tal, crie uma classe chamada Loja que modele uma loja gen´erica.
Essa classe deve ter os seguintes elementos:
• Atributos: nome (string) e lista de Produtos (lista de objetos da classe Produto)
• M´etodos:
– adicionar produto: recebe como parˆametros o nome, o pre¸co e a quantidade do produto,
cria um objeto da classe Produto com essas informa¸c˜oes e adiciona na lista de produtos
da loja
– buscar produto: recebe como parˆametro o nome do produto e retorna o objeto da classe
Produto correspondente, caso exista
– realizar venda: recebe como parˆametros o nome do produto e a quantidade a ser vendida, e realiza a venda do produto correspondente, reduzindo a quantidade dispon´ıvel
– exibir informacoes produtos: exibe na tela as informa¸c˜oes de todos os produtos da loja
Al´em disso, crie uma classe chamada Produto que modele um produto da loja. Essa classe deve
ter os seguintes elementos:
• Atributos: nome (string), pre¸co (float) e quantidade (inteiro)
• M´etodos:
– atualizar quantidade: recebe como parˆametro a quantidade a ser atualizada e atualiza
a quantidade do produto
'''

class Loja():
    def __init__(self, nome_loja, lista_produtos):
        self.nome_loja = nome_loja
        self.lista_produtos = lista_produtos

    def adicionar_produto(self, nome_novo, preco, qtd): 
        produto = Produto(nome_novo, preco, qtd)
        self.lista_produtos.append(produto)

    def consultar_produto(self):
        for produto in self.lista_produtos:
            print(f'Produto: {produto.nome_produto}, Preço: {produto.preco_produto}, Quantidade: {produto.quantidade}')
class Produto():
    def __init__(self, nome_produto, preco_produto, quantidade):
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
        self.quantidade = quantidade

    def atualizar_quantidade(self, qtd_nova):
        self.quantidade = qtd_nova

Loja1 = Loja("Loja do João", [])
Loja1.adicionar_produto("Notebook", 3000.0, 5)
Loja1.adicionar_produto("Mouse", 50.0, 10)
Loja1.consultar_produto()
