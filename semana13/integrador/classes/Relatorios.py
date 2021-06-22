from abc import ABC, abstractmethod
import csv

class Relatorios(ABC):
    @abstractmethod
    def criar_relatorio(self, lista):
        pass


class Relatorio_TXT(Relatorios):
    def criar_relatorio(self, lista, nome_arquivo):
        nome_arquivo = nome_arquivo + '.txt'
        with open(nome_arquivo, "w") as f:
            f.write('Relatório de Vendas\n')
            f.write(40 * '*' + '\n')
            f.write("DATA\t\t\t\t VALOR\n")
            for i in lista:
                f.write(str(i[0]) + 8 * " ")
                f.write(str(i[1]) + 7 * " ")
                f.write('\n')
            return True

class Relatorio_CSV(Relatorios):
    def criar_relatorio(self, lista, nome_arquivo):
        path = 'C:/Users/Cesar/Documents/Atividade Napp Academy/NappAcademy semana 02/semana13/'
        nome_arquivo = path + nome_arquivo + '.csv'
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['DATA', 'VALOR'])
            for i in range(len(lista)):
                writer.writerow([lista[i][0], lista[i][1]])
            return True