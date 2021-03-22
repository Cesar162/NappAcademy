from semana7.classes.product import Produtos
from semana7.classes.client import Cliente
from semana7.classes.pedido import Pedido
from semana7.classes.ecommerce import loja

loja = Loja('Loja Napp')
loja.add_product('123', 15, 10)
loja.add_product('1234', 20, 5)
pedido = Pedido(Cliente('José da Silva'))
cliente = Cliente('John Doe')
pedido2 = Pedido(cliente)

pedido.add_item(loja.comprar('1234'))
pedido.add_item(loja.comprar('123'))
pedido.add_item(loja.comprar('1234'))
pedido.add_item(loja.comprar('123'))
pedido2.add_item(loja.comprar('1234'))
pedido2.add_item(loja.comprar('123'))

loja.devolver_carrinho(pedido)
pedido2.checkout('dinheiro')