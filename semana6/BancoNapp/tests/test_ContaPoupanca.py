from BancoNapp.contas.ContaPoupanca import ContaPoupanca
from BancoNapp.contas.Conta import Conta
import pytest


class TestContaPoupanca:
    def test_class_declared(self):
        conta = ContaPoupanca()
        assert isinstance(conta, ContaPoupanca)
        assert issubclass(ContaPoupanca, Conta)

    def test_instanciar_objeto_somente_nome(self):
        conta = ContaPoupanca(nome='John Doe')
        assert conta.nome, 'John Doe'
        assert conta.profissao == ''
        assert conta.saldo == 0
        assert conta.limite == 500

    def test_instanciar_objeto_saldo_padrao(self):
        conta = ContaPoupanca(nome='John Doe', profissao='Dev Java')
        assert conta.nome, 'John Doe'
        assert conta.profissao == 'Dev Java'
        assert conta.saldo == 0
        assert conta.limite == 500

    def test_instanciar_objeto_saldo_positivo(self):
        conta = ContaPoupanca(nome='John Doe', profissao='Dev', saldo=10)
        assert conta.nome, 'John Doe'
        assert conta.profissao, 'Dev'
        assert conta.saldo == 10
        assert conta.limite == 500

    def test_instanciar_objeto_saldo_negativo(self):
        with pytest.raises(ValueError) as error:
            ContaPoupanca(nome='John Doe', profissao='dev', saldo=-10.00)
        assert str(error.value) == 'Saldo negativo'

    def test_limite(self):
        objeto = ContaPoupanca(nome='John Doe', saldo=10.00, limite=1000)
        objeto.deposito(20)
        assert objeto.saldo == 30
        assert objeto.limite == 1000

    depositos_ok = [
        (10, 20, 30),
        (20, 20, 40),
        (10, 0.01, 10.01),
        (10, 0.01, 10.01),
    ]

    @pytest.mark.parametrize("valor_inicial, deposito, valor_f", depositos_ok)
    def test_depositos(self, valor_inicial, deposito, valor_f):
        conta = ContaPoupanca(nome='John Doe', saldo=valor_inicial)
        conta.deposito(deposito)
        assert conta.saldo == valor_f

    depositos_negativos = [
        (10, 0),
        (10, -0.1),
        (10, -1),
        (10, -2),
    ]

    @pytest.mark.parametrize("valor_inicial, deposito", depositos_negativos)
    def test_depositos_com_erro(self, valor_inicial, deposito):
        msg = 'Valor do depósito precisa ser maior que zero'
        with pytest.raises(ValueError) as error:
            conta = ContaPoupanca(nome='John Doe', saldo=valor_inicial)
            conta.deposito(deposito)
        assert str(error.value) == msg

    valores_com_erro = [
        ([15, 12]),
        ((15, 12)),
        (10+2j),
        ('15'),
    ]

    @pytest.mark.parametrize("deposito", valores_com_erro)
    def test_depositos_com_valores_errados(self, deposito):
        with pytest.raises(TypeError) as error:
            conta = ContaPoupanca(nome='John Doe', saldo=10)
            conta.deposito(deposito)
        assert str(error.value) == 'O depósito precisa ser numérico'

    saque_ok = [
        (20, 10, 10),
        (150.10, 150.10, 0.0),
        (150.90, 50.40, 100.50),
        (500.60, 500.20, 0.40),
    ]

    @pytest.mark.parametrize("valor_ini, valor_saque, valor_f", saque_ok)
    def test_saques_ok(self, valor_ini, valor_saque, valor_f):
        conta = ContaPoupanca(nome='John Doe', saldo=valor_ini)
        valor_sacado = conta.saque(valor_saque)
        assert valor_saque == pytest.approx(valor_sacado, 0.001)
        assert conta.saldo == pytest.approx(valor_f, 0.001)

    saque_com_falha = [
        (10, 2000),
        (20, 1000),
        (100, 600),
        (0.90, 1500.90),
        (10.40, 50)        
    ]

    @pytest.mark.parametrize("valor_inicial, valor_saque", saque_com_falha)
    def test_saques_falha(self, valor_inicial, valor_saque):
        msg = 'Valor do saque supera seu saldo.'
        with pytest.raises(ValueError) as error:
            conta = ContaPoupanca(nome='John Doe', saldo=valor_inicial)
            conta.saque(valor_saque)
        assert str(error.value) == msg

    @pytest.mark.parametrize("valor_saque", valores_com_erro)
    def test_saques_com_erro(self, valor_saque):
        with pytest.raises(TypeError) as error:
            conta = ContaPoupanca(nome='John Doe', saldo=10)
            conta.saque(valor_saque)
        assert str(error.value) == 'O valor do saque precisa ser numérico'

    def test_get_extrato_sem_operacoes(self):
        extrato = [('I', 10.55)]
        conta = ContaPoupanca(nome='John Doe', saldo=10.55)
        assert conta.get_extrato() == extrato

    def test_get_extrato_1(self):
        extrato = [('I', 10.55), ('D', 100), ('S', 20), ('S', 25), ('S', 10)]
        conta = ContaPoupanca(nome='John Doe', saldo=10.55)
        conta.deposito(100)
        conta.saque(20)
        conta.saque(25)
        conta.saque(10)
        assert conta.get_extrato() == extrato

    def test_get_extrato_2(self):
        extrato = [('I', 100.55), ('S', 20), ('S', 25), ('S', 10), ('D', 100)]
        conta = ContaPoupanca(nome='John Doe', saldo=100.55)
        conta.saque(20)
        conta.saque(25)
        conta.saque(10)
        conta.deposito(100)
        assert conta.get_extrato() == extrato

    juros_ok = [
        (0, 100),
        (0.1, 100.1),
        (1.0, 101),
        (0.5, 100.5),
        (0.9, 100.9)
    ]

    @pytest.mark.parametrize("juros, valor_final", juros_ok)
    def test_rendimento_aniversario_ok(self, juros, valor_final):
        conta = ContaPoupanca(nome='John Doe', saldo=100)
        conta.rendimento_aniversario(juros=juros, dias=400)
        assert conta.saldo == pytest.approx(valor_final)

    juros_incorretos = [
        (-0.0001),
        (-0.1),
        (1001),
        (101),
    ]

    @pytest.mark.parametrize("juros", juros_incorretos)
    def test_porcentagem_rendimento_maior_que_zero(self, juros): 
        with pytest.raises(ValueError) as error_03:
            conta = ContaPoupanca(nome='John Doe', saldo=10)
            conta.rendimento_aniversario(juros=juros,dias=366)
        assert str(error_03.value) == 'O valor do rendimento deve ser maior que 0'

    juros_incorretos = [
        (-0.0001),
        (-0.1),
        (1001),
        (101),
    ]

    @pytest.mark.parametrize("juros", juros_incorretos)
    def test_porcentagem_rendimento_maior_que_zero(self, juros): 
        with pytest.raises(ValueError) as error_03:
            conta = ContaPoupanca(nome='John Doe', saldo=10)
            conta.rendimento_aniversario(juros=juros,dias=366)
        assert str(error_03.value) == 'O valor do rendimento deve ser maior que 0'


    def test_rendimentos_com_erro(self):
        with pytest.raises(TypeError) as error_01:
            conta = ContaPoupanca(nome='John Doe', saldo=10)
            conta.rendimento_aniversario(juros='juros', dias=305)
        assert str(error_01.value) == 'O juros precisa ser um valor numérico'

    def test_ano_para_rendimento(self):        
        with pytest.raises(TypeError) as error_02:
            obj = ContaPoupanca(nome='John Doe', saldo=10)
            obj.rendimento_aniversario(juros=1, dias='data')
        assert str(error_02.value) == 'A quantidade de dias precisa ser numérico'



