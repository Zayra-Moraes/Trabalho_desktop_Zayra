from package.models.Campeonato import Campeonato

class Equipe():
    todas_equipes_incritas=[]
    def __init__(self, nome, ano):
        self.nome=nome
        self.ano=ano
        self.jogadores=[]
        self.tecnico=None
        self.pontos=0
        self.saldo_de_gols=0
        Equipe.todas_equipes_incritas.append(self)


    def _add_pontos(self,ponto):
        self.pontos+=ponto
    
    def mostrar_pontos(self):
        print(f'O saldo de pontos da Equipe é {self.pontos}')

    def mostrar_saldo_de_gols(self):
        print(f'O saldo de gols da equipe é {self.saldo_de_gols}')

    def add_jogador(self,jogador):
        if jogador not in self.jogadores:
            if len(self.jogadores) < 12:
                self.jogadores.append(jogador)
                jogador.equipe=(self)
            else:
                print(f'Não é possivel adicionar {jogador} na equipe pois ela já tem 12 jogadores.')
        else: 
            print('Jogador já está na equipe.')

    def remover_jogador(self, jogador):
        if jogador in self.jogadores:
            self.jogadores.remove(jogador)
            jogador.equipe=None
            print(f'Jogador foi removido da equipe')
        else:
            return f'O jogador não está nessa equipe'

    def add_tecnico(self,tecnico):
        self.tecnico=tecnico
        tecnico.equipe=(self)

    def remover_tecnico(self, tecnico):
        if tecnico == self.tecnico:
            self.tecnico= None
            tecnico.equipe=None
            return f'Tecnico removido da equipe.'
        else:
            return f'O tecnico não está nessa equipe'

    def mostrar_equipe(self):
        n=1
        if self.tecnico:
            print(f'Equipe: {self.nome} - {self.ano}')
            print(f'Tecnico: {self.tecnico.nome}')
            for i in self.jogadores:
                print(f'{n}- {i.nome}')
                n+=1
        else:
            print(f'Equipe: {self.nome} - {self.ano}')
            for i in self.jogadores:
                print(f'{n}- {i.nome}')
                n+=1

    def excluir_equipe(self):
        if self in self.__class__.todas_equipes_incritas:
            self.__class__.todas_equipes_incritas.remove(self)
            for c in Campeonato.todos_os_campeonatos:
                c.remove_equipe(self)
                print(f'{self.nome} removido do sistema.')
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