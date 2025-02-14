from semana7.classes.pedido import Pedido
from semana7.classes.client import Cliente
from semana7.classes.product import Produto
import pytest

class Test_Pedido:
    def test_class_decladed(self):
        cliente = Cliente('Therezinha de Souza')
        pedido = Pedido(cliente)
        assert isinstance(pedido, Pedido)
        assert pedido.itens == []

    def test_class_decladed_fail(self):
        msg_erro = 'Não é possível instanciar um pedido sem um cliente'
        with pytest.raises(TypeError) as error:
            Pedido('José da Silva')
        assert str(error.value) == msg_erro
    
    def test_str_repr(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        assert str(pedido) == 'Pedido de José da Silva'
        assert repr(pedido) == 'Pedido de José da Silva'
    
    def test_properties(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        assert pedido.cliente.nome == 'José da Silva'
        assert pedido.itens == []
        pedido.itens = [1]
        # assert pedido.itens == [1]

    def test_metodo_add_item(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        produto = Produto(ean = '123456789')
        produto2 = Produto(ean = '987654321')
        pedido.add_item(produto)
        pedido.add_item(produto2)
        assert len(pedido.itens) == 2

    def test_metodo_add_item_fail(self):
        msg_erro = 'Não foi passado um objeto produto'
        with pytest.raises(TypeError) as error:
            cliente = Cliente('José da Silva')
            pedido = Pedido(cliente)
            pedido.add_item('string não produto')
        assert str(error.value) == msg_erro

    def test_quantidade_produto_no_pedido(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        pedido.add_item(Produto(ean = '123'))
        pedido.add_item(Produto(ean = '123'))
        pedido.add_item(Produto(ean = '123456'))
        pedido.add_item(Produto(ean = '123'))
        assert pedido.quantidade_produto_no_pedido('123') == 3
        assert pedido.quantidade_produto_no_pedido('123456') == 1
        assert pedido.quantidade_produto_no_pedido('987') == 0

    def test_nota_fiscal(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        pedido.add_item(Produto(ean='123', preco =10))
        pedido.add_item(Produto(ean='123456', preco =25))
        pedido.add_item(Produto(ean='123', preco =10))
        nota_fiscal = pedido.nota_fiscal()
        assert len(nota_fiscal) == 2
        assert type(nota_fiscal[0]) ==  tuple
    
    def test_valor_total_pagar(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        pedido.add_item(Produto(ean = '123', preco = 20))
        pedido.add_item(Produto(ean = '1234', preco = 40))
        assert pedido.valor_total_pagar() == 60
    
    def test_valor_total_vazio(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        assert pedido.test_valor_total_pagar() == 60
    
    def test_checkout(self):
        cliente = Cliente('José da Silva')
        pedido = Pedido(cliente)
        pedido.add_item(Produto(ean='123', preco=15))
        pedido.add_item(Produto(ean='123456', preco=9))
        pedido.add_item(Produto(ean='123', preco=15))
        checkout = pedido.checkout('dinheiro')
        assert len(checkout) == 2
        assert checkout[1] == 39
    
    def test_checkout_fail(self):
        msg_erro = 'Forma de pagamento não aceita'
        with pytest.raises(Exception) as error:
            cliente = Cliente('José da Silva')
            pedido = Pedido(cliente)
            produto1 = Produto(ean = '123', preco = 15)
            pedido.add_item(produto1)
            pedido.checkout('marcar')
        assert str(error.value) == msg_erro
    
    def test_checkout_fail2(self):
        msg_erro = 'Informe o meio de pagamento'
        with pytest.raises(Exception) as error:
            pedido = Pedido(Cliente('José da Silva'))
            pedido.add_item(Produto(ean = '123', preco = 15))
            pedido.checkout()
        assert str(error.value) == msg_erro