class Pessoa():
    def __init__(self,nome,idade,cpf):
        self.nome=nome
        self._idade=idade
        self._cpf=cpf


    def mostrar_dados(self):
         return f'{self.nome.upper()} || {self._idade} || {self._cpf}'
    
    
    def atualizar_idade(self,nova_idade):
        self._idade=nova_idade

    def atualizar_cpf(self,novo_cpf):
        self._cpf=novo_cpf
