from package.models.Pessoa import Pessoa
from package.models.Equipe import Equipe
from package.controllers.serialjson import DataRecord

class Jogador(Pessoa):
    todos_os_jogadores_inscritos=[]
    db= DataRecord("jogadores.json")
    def __init__(self,nome,_idade,posicao,_cpf,equipe=None, from_json=False):
        super().__init__(nome, _idade, _cpf)
        self.posicao=posicao
        self.equipe=equipe
        Jogador.todos_os_jogadores_inscritos.append(self)
        if not from_json:
            Jogador.db.add(self)
    
    
    @classmethod
    def carregar_todos(cls):
        cls.todos_os_jogadores_inscritos = []

        for data in cls.db.get_all():
            if "idade" in data:
                data["_idade"] = data.pop("idade")
            if "cpf" in data:
                data["_cpf"] = data.pop("cpf")

            # equipe_str = data.get("equipe")
            # if equipe_str:
            #     data["equipe"] = todas_as_equipes.get(equipe_str)
            # else:
            #     data["equipe"] = None

            cls(**data, from_json=True)

    def atualizar_posicao(self,nova_posicao):
        self.posicao=nova_posicao
        self.db.update(self)

    def dados_completos(self):
        if self.equipe == None:
            return f'{super().mostrar_dados()} || {self.posicao}'
        else:
            e=Equipe.find_equipe(self.equipe)
            equipe_nome = e.nome
            return f'{super().mostrar_dados()} || {self.posicao} || {equipe_nome}'

    @classmethod
    def find_jogador(cls,nome1):
        for j in cls.todos_os_jogadores_inscritos:
            if j.nome.lower() == nome1.lower():
                #print(j.dados_completos())
                return j            
        #print(f'Nenhum jogador com esse nome encontrado.')
        return None

    def mostrar_equipe(self):
        if self.equipe == None:
            print(f'O jogador não está em nenhuma equipe')

        else:
            print(f'O jogador está na equipe {self.equipe}')

        
    def excluir_jogador(self):
        if self in self.__class__.todos_os_jogadores_inscritos:
            self.__class__.todos_os_jogadores_inscritos.remove(self)
            nome=self.nome
            for e in Equipe.todas_equipes_incritas:
                e.remover_jogador(nome)
            
            self.db.delete(self)
            return f'{self.nome} removido do sistema.'
        else:
            return 'Jogador não está cadastrado.'
    
    def to_dict(self):
        return {
                "nome": self.nome,
                "_idade": self._idade,
                "_cpf": self._cpf,
                "posicao": self.posicao,
                "equipe": self.equipe.nome if self.equipe else None
                }
    
    @classmethod
    def listar_jogadores_cadastrados(cls):
        print('JOGADORES CADASTRADOS:')
        for j in cls.todos_os_jogadores_inscritos:
            print(j.dados_completos())

Jogador.carregar_todos()

class Tecnico(Pessoa):
    db=DataRecord('tecnicos.json')
    todos_os_tecnicos_incritos=[]
    def __init__(self,nome,_idade,_cpf, licenca, equipe=None, from_json=False):
        super().__init__(nome, _idade, _cpf)
        self._licenca=licenca
        self.equipe=equipe
        Tecnico.todos_os_tecnicos_incritos.append(self)
        if not from_json:
            Tecnico.db.add(self)

    @classmethod
    def carregar_todos(cls):
        for data in cls.db.get_all():
            if "idade" in data:
                data["_idade"] = data.pop("idade")
            if "cpf" in data:
                data["_cpf"] = data.pop("cpf")
            if "_licenca" in data:
                data["licenca"] = data.pop("_licenca")
            cls(**data,from_json=True)

    def dados_completos(self):
        if self.equipe == None:
            return f'{super().mostrar_dados()} || {self._licenca}'
        else:
            e=Equipe.find_equipe(self.equipe)
            equipe_nome= e.nome
            return f'{super().mostrar_dados()} || {self._licenca} || {equipe_nome}'
    
    def mostrar_equipe(self):
        if self.equipe == None:
            print(f'O tecnico não está em nenhuma equipe')

        else:
            print(f'O tecnico está na equipe {self.equipe}')


    def excluir_tecnico(self):
        if self in self.__class__.todos_os_tecnicos_incritos:
            self.__class__.todos_os_tecnicos_incritos.remove(self)
            nome=self.nome
            for e in Equipe.todas_equipes_incritas:
                e.remover_tecnico(nome)
            self.db.delete(self)
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

Tecnico.carregar_todos()