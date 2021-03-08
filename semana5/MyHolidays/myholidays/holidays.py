from datetime import date

class MyCalendar:

    def __init__(self, *args):
        self.datas = []
        self.datas.append(date(2021, 12, 5))
        self.datas.append('25/12/2021')
        # self.datas = append(self.teste_string())
        # self.add_holiday = valor
        #self.datas = [args]

        #self.datas.append(date(2021, 4, 21))
    
    def teste_string(self):
        testeobj = self.datas
        if type(testeobj) == str:
            True
        else:
            raise ValueError("Não consigo passar este tipo de valor")
        