from package.models.Partida import Partida
from package.controllers.serialjson import DataRecord
from package.models.EquipeCampeonato import EquipeCampeonato

class Campeonato():
    todos_os_campeonatos=[]
    db=DataRecord("campeonato.json")
    def __init__(self,nome, from_json=False, **kwargs):
        self.nome=nome
        self.partidas=kwargs.get('partidas',[])
        self.equipes=kwargs.get('equipes',[])
        if self not in Campeonato.todos_os_campeonatos:
            Campeonato.todos_os_campeonatos.append(self)
        if not from_json:
            Campeonato.db.add(self)
    
    @classmethod
    def carregar_todos(cls):
        cls.todos_os_campeonatos=[]
        for data in cls.db.get_all():
            nome = data.get('nome')
            partidas=data.get('partidas',[])
            equipes=data.get('equipes',[])

            campeonato=cls(
                nome=nome,
                partidas=partidas,
                equipes=equipes,
                from_json=True
            )



    def add_equipe(self,equipe):
        from package.models.Equipe import Equipe
        e=Equipe.find_equipe(equipe)
        if e:
            if len(e.jogadores) >= 7 and e.tecnico != None:
                self.equipes.append(equipe)
                e_=EquipeCampeonato.find_equipe_campeonato(e.nome,self.nome)
                if e_ is None:
                    ec = EquipeCampeonato(e.nome, self.nome)
                self.db.update(self)
            elif len(e.jogadores) < 7:
                print(f'A equipe tem menos de 7 jogadores e não pode ser incrita no campeonato.')
            elif e.tecnico == None:
                print(f'A equipe não tem um tecnico cadastrado')
        else:
            print(f'Equipe não encontrada')

    def remover_equipe(self,equipe):
        from package.models.Equipe import Equipe
        e=Equipe.find_equipe(equipe)
        if e:
            if equipe in self.equipes:
                self.equipes.remove(equipe)
                self.db.update(self)
                return f'Equipe removida da competição.'
            else:
                return f'O jogador não está na equipe.'
        else:
            return f'Equipe não encontrada'

    def criar_partida(self,equipe1,equipe2,placar):
        from package.models.Equipe import Equipe
        if equipe1 in self.equipes and equipe2 in self.equipes:
            partida=Partida(equipe1,equipe2,campeonato=self.nome)
            self.partidas.append(partida.id)
            e_1=EquipeCampeonato(equipe1,self.nome)
            e_2=EquipeCampeonato(equipe2,self.nome)
            e1=Equipe.find_equipe(equipe1)
            e2=Equipe.find_equipe(equipe2)
            while True:
                    #placar=input(f"Por favor inserir o placar final da partida: (no formato '2x1')")
                    if 'x' in placar:
                        partes = placar.split('x')
                        if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
                            gols1, gols2 = map(int, partes)
                            partida._definir_placar(gols1, gols2)
                            print(f'Partida finalizada entre {e1.nome} X {e2.nome} - {gols1} X {gols2}')
                            self.db.update(self)
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
            print(f'{n} - {i}')
            n+=1

    def mostrar_partidas(self):
        from package.models.Partida import Partida
        n=1
        print('PARTIDAS:')
        for i in self.partidas:
            p=Partida.find_partida(i["id"])
            print(f'{n}°: {p.mostrar_placar()}')
            n+=1

    def _ordenacao(self,nome_equipes):
        from package.models.Equipe import Equipe
        e=Equipe.find_equipe(nome_equipes)
        return (e.pontos, e.saldo_de_gols)

    def tabela_de_classificacao(self):
        from package.models.Equipe import Equipe
        ranking=sorted(self.equipes, key=self._ordenacao, reverse=True)
        print(f"\n{'Posição':<10}{'Equipe':<15}{'Pontos':<10}{'Saldo de Gols'}")
        print(f'{'-'*55}')
        for posicao, equipe in enumerate(ranking,start=1):
            e=Equipe.find_equipe(equipe)
            print(f"{posicao:<10}{e.nome:<15}{e.pontos:<10}{e.saldo_de_gols}")

    def tabela_de_posicoes(self):
        # Lista de equipes **dentro do campeonato**
        equipes_campeonato = [
            EquipeCampeonato.find_equipe_campeonato(equipe, self.nome)
            for equipe in self.equipes
        ]

        # remove possíveis None
        equipes_campeonato = [e for e in equipes_campeonato if e]

        # Ordenar pelas pontuações DO CAMPEONATO
        ranking = sorted(
            equipes_campeonato,
            key=lambda e: (e.pontos, e.saldo_de_gols),
            reverse=True
        )

        # Construir tabela
        tabela = []
        for posicao, e in enumerate(ranking, start=1):
            tabela.append({
                'posicao': posicao,
                'nome': e.nome,
                'pontos': e.pontos,
                'saldo': e.saldo_de_gols
            })

        return tabela
    
    def excluir_campeonato(self):
        if self in self.__class__.todos_os_campeonatos:
            self.__class__.todos_os_campeonatos.remove(self)
            self.db.delete(self)
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


Campeonato.carregar_todos()