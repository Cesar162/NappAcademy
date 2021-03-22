# class Produtos:
#     def __init__(self, codigo_ean, preco):
#         self._codigo_ean = codigo_ean
#         self._preco = preco

class Produto:
    def __init__(self, **kwargs):
        if kwargs.get('preco', 0) < 0:
            raise ValueError('Preço negativo')
        self._codigo_ean = kwargs.get('ean', '')
        self._preco = kwargs.get('preco', 0)

    # O @property funciona como get, de modo que é possível
    # seta-los mediante o @NOME DO METODO.setter, o que permite alterar o valor que deseja manipular
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, value):
        self._preco = value
    
    @property
    def ean(self):
        return self._codigo_ean

    @ean.setter
    def ean(self, value):
        self._codigo_ean = value 

    # Permite que o codigo tenha um retorno de valor mais amigavel
    def __str__(self):
        return self._codigo_ean
    
    # Cria uma representação do objeto com o valor atribuido a ele
    def __repr__(self):
        return 'Produto: ' + self._codigo_ean