from rh.classes.Colaborador import Colaborador

class Departamento:
    def __init__(self, nome_setor, responsavel):
        if type(nome_setor) != str or type(responsavel) != str:
            raise TypeError('Foi digitado um número ao invés de um nome')

        self._nome_setor = nome_setor
        self._responsavel = responsavel
        self._colaboradores = []

    @property
    def nome(self):
        return self._nome_setor

    @nome.setter
    def nome(self, value):
        self._nome_setor = value

    @property
    def responsavel(self):
        if self._responsavel is None:
            return None
        return str(self._responsavel)
    
    @responsavel.setter
    def responsavel(self, value):
        self._responsavel = value

    @property
    def colaboradores(self):
        return self._colaboradores

    def trocar_responsavel(self, nome, dep):
        if nome != self.responsavel or dep != self._nome_setor:
            self._responsavel = nome
            self._nome_setor = dep
        else:
            raise ValueError('O nome ou departamento é diferentes do que se encontra cadastrado')

    def informar_responsavel(self, **kwargs):
        if kwargs.get('ano','') < 1950:
            raise ValueError('A idade informada é menor que a permitida') 
        if kwargs.get('nome','') == self._responsavel:
            self._colaboradores.append(Colaborador(self._responsavel, kwargs.get('dia',''), kwargs.get('mes',''), kwargs.get('ano',''), self._nome_setor))
        else:
            raise ValueError('O nome informado não corresponde ao nome cadastrado')
    
    def add_colaborador(self, **kwargs):
        if kwargs.get('ano','') < 1950:
            raise ValueError('A idade informada é menor que a permitida')
        self._colaboradores.append(Colaborador(kwargs.get('nome', ''), kwargs.get('dia',''), kwargs.get('mes',''), kwargs.get('ano',''), self._nome_setor))

    def verificar_aniversariantes(self):
        lista = []
        for colaborador in self.colaboradores:
            if colaborador.aniversario_hoje():
                lista.append((colaborador.nome, colaborador.aniversario, colaborador.departamento))
        return lista

    def __str__(self):
        return self._nome_setor

    def __repr__(self):
        return 'Departamento = ' + self._nome_setor
