from semana7.classes.product import Produto
from semana7.classes.pedido import Pedido

class Loja:
   
    def __init__(self, nome = 'Lojas Americanas'):
        if type(nome) != str:
            raise ValueError('O valor passado é um número')
        self._nome = nome
        self._estoque = []
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def estoque(self):
        return self._estoque

    def __str__(self):
        return self._nome

    def __repr__(self):
        return 'Lojas => ' + self._nome   

    def add_product(self, ean, preco, quantidade):
        if quantidade < 1:
            raise ValueError('O produto encontra-se em falta')
        for i in range(quantidade):
            self._estoque.append(Produto(ean = ean, preco = preco))
    
    def quantidade_produto(self, ean):
        # quantidade = None
        # cod = Produtos(ean= ean)
        # quantidade = self._estoque.count(cod._codigo_ean) 
        # return quantidade

        quantidade = 0
        for produto in self._estoque:
            if produto._codigo_ean == ean:
                quantidade = quantidade + 1
        return quantidade

    def comprar(self, ean):
        # if self._estoque.count(str(ean)) > 0:
        #     prod_comprado = self._estoque.pop(self._estoque.index(str(ean)))
        #     return prod_comprado
        # else:
        #     return None

        for produto in self._estoque:
            if str(produto) == ean:
                self._estoque.remove(produto)
                return produto
        return None     

    def devolver_carrinho(self, pedido):
        if isinstance(pedido, Pedido):
            for item in pedido.itens:
                if isinstance(item, Produtos):
                    self._estoque.append(item)
            pedido.itens = []
            return pedido



    
    

