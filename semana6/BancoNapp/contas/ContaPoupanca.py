from BancoNapp.contas.Conta import Conta

class ContaPoupanca(Conta):
   def __init__(self,  **kwargs):
      """
      Construtor da classe PessoaFísica.
      Extrai do dicionário kwargs a profissao do correntista.
      """
      self.profissao = kwargs.get('profissao', '')
      super(ContaPoupanca, self).__init__(**kwargs)

   def deposito(self, valor):
      if isinstance(valor, (float, int)):
         if valor <= 0:
            raise ValueError('Valor do depósito precisa ser maior que zero')
         self.saldo = self.saldo + valor
         self.extrato.append(('D', valor))
         return
      raise TypeError('O depósito precisa ser numérico')

   def saque(self, valor):
      if isinstance(valor, (float, int)):
         if valor > self.saldo:
            raise ValueError('Valor do saque supera seu saldo.')
            return
         self.saldo = self.saldo - valor
         self.extrato.append(('S', valor))
         return valor
      raise TypeError('O valor do saque precisa ser numérico')

   def rendimento_aniversario(self, **kwargs):
      if type(kwargs.get('juros','')) != float and type(kwargs.get('juros','')) != int:
         raise TypeError('O juros precisa ser um valor numérico')

      if type(kwargs.get('dias','')) != int:
         raise TypeError('A quantidade de dias precisa ser numérico')

      if kwargs.get('juros','') < 0 or kwargs.get('juros','') > 1:
         raise ValueError('O valor do rendimento deve ser maior que 0')
      
      if kwargs.get('dias','') > 365:
         self._juros = kwargs.get('juros','')
         self.saldo = self.saldo + self._juros 
         self.extrato.append(('S', self.saldo))
         return self.saldo

   def get_extrato(self):
      """
      Retorna a lista dos saques e depósitos feitos na conta.

      Returns:
         List: Lista de operações
      """
      return self.extrato

