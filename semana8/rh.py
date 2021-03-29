from rh.classes.Departamento import Departamento

from datetime import date, timedelta
dt1 = date.today() - timedelta(days=4)
hoje = date.today()

departamento = Departamento('Departamento XYZ', 'Julia Mendes')
departamento.informar_responsavel(nome='Julia Mendes', dia=dt1.day, mes=dt1.month, ano=1990)
departamento.add_colaborador(nome='João Oliveira', dia=hoje.day, mes=hoje.month, ano=1992)
departamento.add_colaborador(nome='Pedro Mendonça', dia=dt1.day, mes=dt1.month, ano=1993)
departamento.add_colaborador(nome='Luis Fernando', dia=hoje.day, mes=hoje.month, ano=2000)
departamento.add_colaborador(nome='Maurício Souza', dia=dt1.day, mes=dt1.month, ano=1985)

aniversariantes = departamento.verificar_aniversariantes()

for aniversariante in aniversariantes:
    print('Parabéns ' + aniversariante[0] + ' pelo seu dia')
