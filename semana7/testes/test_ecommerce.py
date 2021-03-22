from semana7.classes.ecommerce import Loja
from semana7.classes.client import Cliente
from semana7.classes.pedido import Pedido
import pytest

class Test_Loja:
    def test_class_decladed(self):
        objeto = Loja('Loja Panamenha')
        assert isinstance(objeto, Loja)

    def test_instanciar_um_objeto(self):
        objeto = Loja('Lojas Colombianas') # Cria uma objeto seu valor já definido
        assert objeto._nome, 'Lojas Colombianas' # Verifica se o valor atribuido a objeto é igual ao verificado

    def nome_setter():
        objeto = Loja()
        assert objeto._nome == 'Lojas Americanas'
        objeto = Loja('Magazine Huguinho')
        assert objeto._nome == 'Magazine Huguinho'
        objeto2 = ()
        assert objeto._estoque == []

    def test_instanciar_valor_diferente_de_string(self):
        with pytest.raises(ValueError) as error:
            Loja(5)
        assert str(error.value) == 'O valor passado é um número'

    def test_str_repr(self):
        objeto = Loja('Casas Gauchas')
        assert str(objeto) == 'Casas Gauchas'
        assert repr(objeto) == 'Lojas => Casas Gauchas'

    def test_adicionar_estoque(self):
        loja = Loja('Ponto Quente')
        loja.add_product('123456789', 50.00, 5)
        assert len(loja.estoque) == 6

    def test_adicionar_estoque(self):
        loja = Loja('Ponto Quente')
        loja.add_product('123456789', 20.00, 8)
        loja.add_product('123456789', 150.00, 4)
        assert len(loja.estoque) == 12
    
    def verificar_quantidade_negativa(self):
        with raises(ValueError) as error:
            Loja.add_product('123', 85.00, -5)
        assert str(error.value) == 'O produto encontra-se em falta'

    def verificar_quantidade_produtos(self):
        loja = Loja('Subterraneo')
        loja.add_product('123', 85.00, 13)
        loja.add_product('1234', 26.99, 20)
        loja.add_product('987654', 74.50, 40)
        loja.add_product('654321', 9.90, 100)
        assert loja.quantidade_produtos('123') == 13
        assert loja.quantidade_produtos('1234') == 20
        assert loja.quantidade_produtos('987654') == 40
        assert loja.quantidade_produtos('654321') == 100
    
    def test_compra(self):
        objeto = Loja('Lojas Lemense')
        objeto.add_product('123', 2.99, 4)
        assert len(objeto._estoque) == 4
        objeto.comprar('123')
        assert len(objeto._estoque) == 3

    def test_comprar_sem_produto(self):
        loja = Loja('Varejão 123')
        loja.comprar('123')
        assert len(loja.estoque) == 0
        assert loja.comprar('123456789') is None

    def test_devolver_carrinho(self):
        loja = Loja('Lojão da China')
        loja.add_product('123', 15, 10)
        loja.add_product('1234', 20, 5)
        assert len(len.estoque) == 15
        cliente = Cliente('John Doe')
        pedido = Pedido(cliente)
        pedido.add_item(loja.comprar('1234'))   
        pedido.add_item(loja.comprar('123'))
        assert len(pedido.itens) == 2
        assert len(loja.estoque) == 13
        assert loja.quantidade_produto('1234') == 4
        assert loja.quantidade_produto('123') == 9
        loja.devolver_carrinho(pedido)
        assert len(pedido.itens) == 0
        assert len(pedido.estoque) == 15

