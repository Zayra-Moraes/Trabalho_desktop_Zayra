from Partida import Partida
class Campeonato():
    todos_os_campeonatos=[]
    def __init__(self,nome):
        self.nome=nome
        self.partidas=[]
        self.equipes=[]
        Campeonato.todos_os_campeonatos.append(self)
        
    def add_equipe(self,equipe):
        if len(equipe.jogadores) >= 7 and equipe.tecnico != None:
            self.equipes.append(equipe)
        elif len(equipe.jogadores) < 7:
            print(f'A equipe tem menos de 7 jogadores e não pode ser incrita no campeonato.')
        elif equipe.tecnico == None:
            print(f'A equipe não tem um tecnico cadastrado')

    def remover_equipe(self,equipe):
        if equipe in self.equipes:
            self.equipes.remove(equipe)
            return f'Equipe removida da competição.'
        else:
            return f'O jogador não está na equipe.'

    def criar_partida(self,equipe1,equipe2,placar):
        if equipe1 in self.equipes and equipe2 in self.equipes:
            partida=Partida(equipe1,equipe2)
            self.partidas.append(partida)
            while True:
                    #placar=input(f"Por favor inserir o placar final da partida: (no formato '2x1')")
                    if 'x' in placar:
                        partes = placar.split('x')
                        if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
                            gols1, gols2 = map(int, partes)
                            partida._definir_placar(gols1, gols2)
                            print(f'Partida finalizada entre {equipe1.nome} X {equipe2.nome} - {gols1} X {gols2}')
                            break
                        else:
                            print("Formato inválido! Use apenas números antes e depois do 'x'.")
                    else:
                        print("Formato inválido do placar! Use o formato '2x1'.")
        else:
            print('Uma das equipes não está incrita no campeonato.')
        

    def mostrar_equipes(self):
        n=1
        print('EQUIPES DO CAMPEONATO:')
        for i in self.equipes:
            print(f'{n} - {i.nome}')
            n+=1

    def mostrar_partidas(self):
        n=1
        print('PARTIDAS:')
        for i in self.partidas:
            print(f'{n}°: {i.mostrar_placar()}')
            n+=1

    def _ordenacao(self,e):
        return (e.pontos, e.saldo_de_gols)

    def tabela_de_classificacao(self):
        ranking=sorted(self.equipes, key=self._ordenacao, reverse=True)
        print(f"\n{'Posição':<10}{'Equipe':<15}{'Pontos':<10}{'Saldo de Gols'}")
        print(f'{'-'*55}')
        for posicao, equipe in enumerate(ranking,start=1):
            print(f"{posicao:<10}{equipe.nome:<15}{equipe.pontos:<10}{equipe.saldo_de_gols}")
    
    def excluir_campeonato(self):
        if self in self.__class__.todos_os_campeonatos:
            self.__class__.todos_os_campeonatos.remove(self)
            print(f'{self.nome} removido do sistema.')
        else:
            print('Campeonato não está cadastrado.')
    
    @classmethod
    def find_campeonato(cls,nome):
        for c in cls.todos_os_campeonatos:
            if c.nome.lower() == nome.lower():
                #print('Campeonato encontrado')
                return c  
        #print(f'Nenhum campeonato com esse nome encontrado.')
        return None

    @classmethod
    def listar_todos_campeonatos(cls):
        n=1
        print('CAMPEONATOS CADASTRADAS:')
        for c in cls.todos_os_campeonatos:
            print(f'{n} - {c.nome}')
        n+=1
