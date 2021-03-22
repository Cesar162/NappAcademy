from semana7.classes.client import Cliente
import pytest

class Test_Cliente:
    def test_class_decladed(self):
        objeto = Cliente(nome = 'Gabe Logan')
        assert isinstance(objeto, Cliente)

    def test_instanciar_objeto(self):
        objeto = Cliente('Johnny Cash')
        assert objeto._nome, 'Johnny Cash'

    def test_instanciar_valor_diferente_string(self):
        with pytest.raises(ValueError) as error:
            Cliente(nome = 10)
        assert str(error.value) == 'Você passou um numero'

    def test_properties(self):
        objeto = Cliente()
        assert objeto.nome == 'Cesar'
        objeto = Cliente('Elvis Presley')
        assert objeto.nome == 'Elvis Presley'

    def test_str_repr(self):
        objeto = Cliente('Bob Dylan')
        assert str(objeto) == 'Bob Dylan'
        assert repr(objeto) == 'Cliente => Bob Dylan'
