from produtos.classes.Produtos import GuaranaAntartica, Dolly, Produto
from produtos.classes.Produtos import CocaCola
from produtos.classes.Produtos import Pepsi
from produtos.classes.Caracteristicas import Tamanho600ml
from produtos.classes.Caracteristicas import Tamanho2litros
from produtos.classes.Caracteristicas import Tamanho3litros
import pytest


class TestColaborador:
    def test_class_Pepsi(self):
        msg = 'Pepsi tamanho: 600ml.'
        objeto = Pepsi(Tamanho600ml())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Pepsi)
        assert objeto.operation() == msg

    def test_class_CocaCola(self):
        msg = 'CocaCola tamanho: 600ml.'
        objeto = CocaCola(Tamanho600ml())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, CocaCola)
        assert objeto.operation() == msg

    def test_class_CocaCola(self):
        msg = 'CocaCola tamanho: 600ml.'
        objeto = CocaCola(Tamanho2litros())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, CocaCola)
        assert objeto.operation() == msg

    def test_class_CocaCola(self):
        msg = 'Guaraná Antartica tamanho: 3 litros.'
        objeto = GuaranaAntartica(Tamanho3litros())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, GuaranaAntartica)
        assert objeto.operation() == msg

    def test_class_abstractClass(self):
        msg_erro = "Can't instantiate abstract class Produto "
        msg_erro = msg_erro + "with abstract methods operation"
        with pytest.raises(TypeError) as error:
            Produto()
        assert str(error.value) == msg_erro
