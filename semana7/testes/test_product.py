from semana7.classes.product import Produto
import pytest

class Test_Produto:
    def test_class_decladed(self):
        objeto = Produto()
        assert isinstance(objeto, Produto)

    def test_instanciar_objeto_somente_ean(self):
        objeto = Produto(ean='123456789') 
        assert objeto._codigo_ean, '123456789'
        assert objeto._preco == 0

    def test_insraciar_objeto_preco_negativo(self):

        # Verifica se ele não permite entradas com valores negativos
        with pytest.raises(ValueError) as error: # Cria um ValueError como error
            Produto(ean = '123456789', preco = -1) # Instancia a classe Produto definindo alguns valores a ela
        assert str(error.value) == 'Preço negativo' # Aqui define que na existencia de uma ValueError, ambas as mensagens devem ser iguais
    
    def test_setter_preco(self):
        # Verifica se a função @preco.setter esta funcionando    
        objeto = Produto()
        assert objeto._preco == 0
        objeto._preco = 100
        assert objeto.preco == 100
        objeto2 = Produto(ean = '1234')
        assert objeto2._codigo_ean == '1234'


        



    
