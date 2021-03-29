from rh.classes.Departamento import Departamento
from datetime import date, timedelta
import pytest


class TestDepartamento:
    def test_class_declared(self):
        objeto = Departamento('Departamento XYZ', 'Fátima')
        assert isinstance(objeto, Departamento)

    def test_instanciar(self):
        objeto = Departamento('Departamento XYZ', 'Rafael')
        assert objeto.nome == 'Departamento XYZ'
        assert objeto.responsavel == 'Rafael'
    
    def test_tipo_entrada(self):
        with pytest.raises(TypeError) as error: 
            Departamento(254, 123) 
        assert str(error.value) == 'Foi digitado um número ao invés de um nome' 

    def test_str_repr(self):
        objeto = Departamento('Departamento XYZ', 'Fátima')
        assert str(objeto) == 'Departamento XYZ'
        assert repr(objeto) == 'Departamento = Departamento XYZ'

    def test_setters(self):
        objeto = Departamento('Curadoria', 'Rafael')
        assert objeto.nome == 'Curadoria'
        objeto.nome = 'ETL'
        assert objeto.nome == 'ETL'
        objeto.responsavel = 'Daniela'
        assert objeto.responsavel == 'Daniela'

    def test_properties(self):
        objeto = Departamento('Departamento XYZ', 'Fátima')
        assert objeto.nome == 'Departamento XYZ'

    def test_ano_nascimento_limite(self):
        obj = Departamento('Departamento Pessoal','Sebastião Caveirinha')
        with pytest.raises(ValueError) as error:
            obj.add_colaborador(nome='Sebastião Caveirinha', dia= 20,mes= 7, ano=1850)
            obj.add_colaborador(nome='Astolfo Melhor Idade', dia= 2, mes= 3, ano= 1941)   
        assert str(error.value) == 'A idade informada é menor que a permitida' 

    def test_responsavel(self):
        departamento = Departamento('Departamento XYZ', 'Fátima')
        assert departamento.responsavel == 'Fátima'
        departamento.informar_responsavel(nome='Fátima', dia=1, mes=1, ano=1990)
        assert departamento.responsavel == 'Fátima'
        assert departamento.nome == 'Departamento XYZ'

    def verificar_nome_responsavel(self):
        dep = Departamento('Curadoria', 'Rafael habermann')
        with pytest.raises(ValueError) as error:
            dep.informar_responsavel(nome='Cesar Brandt', dia=23, mes=5, ano=1992)
        assert str(error.value) == 'O nome informado não corresponde ao nome cadastrado'

    def test_trocar_responsavel(self):
        departamento = Departamento('Departamento XYZ', 'Gustavo')
        assert departamento.responsavel == 'Gustavo'
        departamento.trocar_responsavel('José da Silva', 'Departamento XYZ')
        assert departamento.responsavel == 'José da Silva'
        departamento.trocar_responsavel('João Oliveira', 'Departamento XYZ')
        assert departamento.responsavel == 'João Oliveira'

    def test_add_colaborador(self):
        departamento = Departamento('Departamento XYZ', 'Fátima')
        departamento.informar_responsavel(nome='Fátima', dia=1, mes=1, ano=1990)
        departamento.add_colaborador(nome='João Oliveira', dia=18, mes=3, ano=1992)
        departamento.add_colaborador(nome='Pedro Mendonça', dia=18, mes=4, ano=1993)
        assert len(departamento.colaboradores) == 3

    def test_verificar_aniversariantes(self):
        dt1 = date.today() - timedelta(days=4)
        hoje = date.today()
        if hoje.month < 10:
            mes = '0'+ str(hoje.month)
        else:
            mes = str(hoje.month)
        retorno = [('João Oliveira', '1992-'+str(mes)+'-'+str(hoje.day), 'Departamento XYZ'),
                    ('Luis Fernando',   '2000-'+str(mes)+'-'+str(hoje.day), 'Departamento XYZ')]
        depto = Departamento('Departamento XYZ', 'Fátima')
        depto.informar_responsavel(nome='Fátima', dia=dt1.day, mes=dt1.month, ano=1990)
        depto.add_colaborador(nome='João Oliveira', dia=hoje.day, mes=dt1.month  , ano=1992)
        depto.add_colaborador(nome='Pedro Mendonça', dia=dt1.day, mes=dt1.month  , ano=1993)
        depto.add_colaborador(nome='Luis Fernando', dia=hoje.day, mes=dt1.month  , ano=2000)
        depto.add_colaborador(nome='Maurício Souza', dia=dt1.day, mes=dt1.month  , ano=1958)
        aniversariantes = depto.verificar_aniversariantes()
        print(aniversariantes)
        assert aniversariantes == retorno
        assert len(aniversariantes) == 2
        assert len(aniversariantes[0]) == 3
        assert type(aniversariantes[0]) == tuple
        assert type(aniversariantes) == list
    
    def verificar_departamento_do_colaborador(self):
        depto = Departamento('Departamento XYZ', 'Fátima')
        depto.informar_responsavel(nome='Fátima', dia=dt1.day, mes=dt1.month, ano=1990)
        depto.add_colaborador(nome='João Oliveira', dia=hoje.day, mes=dt1.month  , ano=1992)
        depto.add_colaborador(nome='Pedro Mendonça', dia=dt1.day, mes=dt1.month  , ano=1993)
        depto.add_colaborador(nome='Luis Fernando', dia=hoje.day, mes=dt1.month  , ano=2000)
        depto.add_colaborador(nome='Maurício Souza', dia=dt1.day, mes=dt1.month  , ano=1958)
        assert 'Departamento XYZ' in depto._colaboradores[0]

