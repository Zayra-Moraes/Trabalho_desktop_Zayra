from package.models.Campeonato import Campeonato
from package.controllers.serialjson import DataRecord

class Equipe():
    todas_equipes_incritas=[]
    db=DataRecord('equipes.json')
    def __init__(self, nome, ano,pontos=0,saldo_de_gols=0,from_json=False,**kwargs):
        self.nome=nome
        self.ano=ano
        self.jogadores=kwargs.get('jogadores',[])
        self.tecnico=kwargs.get('tecnico')
        self.pontos=kwargs.get('pontos') or pontos
        self.saldo_de_gols=kwargs.get('saldo_de_gols', saldo_de_gols)
        if self not in Equipe.todas_equipes_incritas:
            Equipe.todas_equipes_incritas.append(self)
        if not from_json:
            Equipe.db.add(self)

    # @classmethod
    # def carregar_equipes(cls):
    #     for data in cls.db.get_all():
    #         nome=data.get('nome')
    #         ano=data.get('ano')
    #         cls(nome, ano, from_json=True)
        
    @classmethod
    def carregar_equipes(cls):
        cls.todas_equipes_incritas = [] 

        for data in cls.db.get_all():
            nome = data.get('nome')
            ano = data.get('ano')
            jogadores = data.get('jogadores', [])
            tecnico = data.get('tecnico')
            pontos = data.get('pontos', 0)
            saldo_de_gols = data.get('saldo_de_gols', 0)


            equipe = cls(
                nome=nome,
                ano=ano,
                pontos=pontos,
                saldo_de_gols=saldo_de_gols,
                from_json=True,
                jogadores=jogadores,
                tecnico=tecnico
            )


    def _add_pontos(self,ponto):
        self.pontos=int(self.pontos)+(ponto)
        self.db.update(self)
    
    def mostrar_pontos(self):
        print(f'O saldo de pontos da Equipe é {self.pontos}')

    def mostrar_saldo_de_gols(self):
        print(f'O saldo de gols da equipe é {self.saldo_de_gols}')

    def add_jogador(self,jogador):
        from package.models.Jogador_e_Tecnico import Jogador
        j=Jogador.find_jogador(jogador)
        if j:  
            if jogador not in self.jogadores:
                if len(self.jogadores) < 12:
                    self.jogadores.append(jogador)
                    nome_equipe=self.nome
                    j.equipe= nome_equipe
                    j.db.update(j)
                    self.db.update(self)
                else:
                    print(f'Não é possivel adicionar {jogador} na equipe pois ela já tem 12 jogadores.')
            else: 
                print('Jogador já está na equipe.')

    def remover_jogador(self, jogador):
        from package.models.Jogador_e_Tecnico import Jogador
        if jogador in self.jogadores:
            self.jogadores.remove(jogador)
            j=Jogador.find_jogador(jogador)
            j.equipe=None
            j.db.update(j)
            Equipe.db.update(self)
            print(f'Jogador foi removido da equipe')
        else:
            print( f'O jogador não está nessa equipe')

    def add_tecnico(self,tecnico):
        from package.models.Jogador_e_Tecnico import Tecnico
        t=Tecnico.find_tecnico(tecnico)
        if self.tecnico == None:
            if t:
                self.tecnico=tecnico
                t.equipe= self.nome
                t.db.update(t)
                Equipe.db.update(self)
            else:
                print('Técnico não encontrado')
        else:
            nome_t_antigo=self.tecnico
            t_antigo=Tecnico.find_tecnico(nome_t_antigo)
            t_antigo.equipe=None
            t_antigo.db.update(t_antigo)
            if t:
                self.tecnico=tecnico
                t.equipe= self.nome
                t.db.update(t)
                Equipe.db.update(self)
            else:
                print('Técnico não encontrado')

    def remover_tecnico(self, tecnico):
        from package.models.Jogador_e_Tecnico import Tecnico
        if tecnico == self.tecnico:
            self.tecnico= None
            Equipe.db.update(self)
            t=Tecnico.find_tecnico(tecnico)
            t.equipe=None
            t.db.update(t)
            return f'Tecnico removido da equipe.'
        else:
            return f'O tecnico não está nessa equipe'

    def mostrar_equipe(self):
        from package.models.Jogador_e_Tecnico import Jogador,Tecnico
        n=1
        if self.tecnico:
            print(f'Equipe: {self.nome} - {self.ano}')
            print(f'Tecnico: {self.tecnico}')
            for i in self.jogadores:
                j=Jogador.find_jogador(i)
                print(f'{n}- {j.nome}')
                n+=1
        else:
            print(f'Equipe: {self.nome} - {self.ano}')
            for i in self.jogadores:
                print(f'{n}- {i}')
                n+=1

    def excluir_equipe(self):
        from package.models.Jogador_e_Tecnico import Jogador,Tecnico
        if self in self.__class__.todas_equipes_incritas:
            self.__class__.todas_equipes_incritas.remove(self)
            for j in Jogador.todos_os_jogadores_inscritos:
                if j.equipe == self.nome:
                    j.equipe == None
                    j.db.update(j)

            for c in Campeonato.todos_os_campeonatos:
                c.remove_equipe(self)
                print(f'{self.nome} removido do sistema.')
            self.db.delete(self)
        else:
            print('Equipe não está cadastrado.')

    @classmethod
    def find_equipe(cls,nome):
        for e in cls.todas_equipes_incritas:
            if e.nome.lower() == nome.lower():
                #print(e.mostrar_equipe())
                return e            
        #print(f'Nenhuma equipe com esse nome encontrada.')
        return None
    
    @classmethod
    def listar_equipes_cadastradas(cls):
        n=1
        print('EQUIPES CADASTRADAS:')
        for e in cls.todas_equipes_incritas:
            print(f'{n} - {e.nome}')
            n+=1

Equipe.carregar_equipes()