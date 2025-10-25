from package.models.Pessoa import Pessoa
from package.models.Equipe import Equipe

class Jogador(Pessoa):
    todos_os_jogadores_inscritos=[]
    def __init__(self,nome,_idade,posicao,_cpf):
        super().__init__(nome, _idade, _cpf)
        self.posicao=posicao
        self.equipe=None
        Jogador.todos_os_jogadores_inscritos.append(self)

    def atualizar_posicao(self,nova_posicao):
        self.posicao=nova_posicao

    def dados_completos(self):
        if self.equipe == None:
            return f'{super().mostrar_dados()} || {self.posicao}'
        else:
            return f'{super().mostrar_dados()} || {self.posicao} || {self.equipe.nome}'

    @classmethod
    def find_jogador(cls,nome):
        for j in cls.todos_os_jogadores_inscritos:
            if j.nome.lower() == nome.lower():
                #print(j.dados_completos())
                return j            
        #print(f'Nenhum jogador com esse nome encontrado.')
        return None

    def mostrar_equipe(self):
        if self.equipe == None:
            print(f'O jogador não está em nenhuma equipe')

        else:
            print(f'O jogador está na equipe {self.equipe.nome}')
        
    def excluir_jogador(self):
        if self in self.__class__.todos_os_jogadores_inscritos:
            self.__class__.todos_os_jogadores_inscritos.remove(self)
            for e in Equipe.todas_equipes_incritas:
                e.remover_jogador(self)
            return f'{self.nome} removido do sistema.'
        else:
            return 'Jogador não está cadastrado.'
    
    @classmethod
    def listar_jogadores_cadastrados(cls):
        print('JOGADORES CADASTRADOS:')
        for j in cls.todos_os_jogadores_inscritos:
            print(j.dados_completos())

class Tecnico(Pessoa):
    todos_os_tecnicos_incritos=[]
    def __init__(self,nome,_idade,_cpf, licenca):
        super().__init__(nome, _idade, _cpf)
        self._licenca=licenca
        self.equipe=None
        Tecnico.todos_os_tecnicos_incritos.append(self)
    
    def dados_completos(self):
        if self.equipe == None:
            return f'{super().mostrar_dados()} || {self._licenca}'
        else:
            return f'{super().mostrar_dados()} || {self._licenca} || {self.equipe.nome}'
    
    def mostrar_equipe(self):
        if self.equipe == None:
            print(f'O tecnico não está em nenhuma equipe')

        else:
            print(f'O tecnico está na equipe {self.equipe.nome}')


    def excluir_tecnico(self):
        if self in self.__class__.todos_os_tecnicos_incritos:
            self.__class__.todos_os_tecnicos_incritos.remove(self)
            for e in Equipe.todas_equipes_incritas:
                e.remover_tecnico(self)
            print(f'{self.nome} removido do sistema.')
        else:
            print('Jogador não está cadastrado.')

    @classmethod
    def find_tecnico(cls,nome):
        for t in cls.todos_os_tecnicos_incritos:
            if t.nome.lower() == nome.lower():
                #print(t.dados_completos())
                return t           
        #print(f'Nenhum técnico com esse nome encontrado.')
        return None
    
    @classmethod
    def listar_tecnicos_cadastrados(cls):
        print('TÉCNICOS CADASTRADOS:')
        for t in cls.todos_os_tecnicos_incritos:
            print(t.dados_completos())