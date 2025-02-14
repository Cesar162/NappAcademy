from datetime import date


class Colaborador:
    def __init__(self, nome, dia=None, mes=None, ano=None, dep='Sem departamento'):
        self._nome = nome
        self._departamento = dep
        try:
            self._aniversario = date(ano, mes, dia)
        except TypeError:
            raise TypeError('Informe dia, mês e ano')

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, value):
        self._departamento = value

    @property
    def aniversario(self):
        return self._aniversario.isoformat()

    def aniversario_hoje(self):
        hoje = date.today()
        if self._aniversario.day == hoje.day:
            if self._aniversario.month == hoje.month:
                return True
        return False

    def __str__(self):
        return self._nome

    def __repr__(self):
        return 'Colaborador: ' + self._nome
