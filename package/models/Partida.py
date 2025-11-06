from package.controllers.serialjson import DataRecord
class Partida():

    todas_as_partidas=[]    
    db=DataRecord('partidas.json')
    def __init__(self, equipe1, equipe2,gols_e1=0,gols_e2=0, vencedor=None):
        self.equipe1=equipe1
        self.equipe2=equipe2
        self.vencedor=vencedor
        self.gols_e1=gols_e1
        self.gols_e2=gols_e2
        if self not in Partida.todas_as_partidas:
            Partida.todas_as_partidas.append(self)
    
    def to_dict(self):
        return {
            "equipe1": self.equipe1,
            "equipe2": self.equipe2,
            "gols_e1": self.gols_e1,
            "gols_e2": self.gols_e2,
            "vencedor": self.vencedor
        }

    @classmethod
    def carregar_todos(cls):
        from package.models.Campeonato import Campeonato
        cls.todas_as_partidas.clear()
        for camp in Campeonato.db.get_all():
            for p in camp.get("partidas", []):
                partida=cls(**p)
                cls.todas_as_partidas.append(partida)


    def _definir_placar(self, resultado_e1, resultado_e2):
        from package.models.Equipe import Equipe
        e1=Equipe.find_equipe(self.equipe1)
        e2= Equipe.find_equipe(self.equipe2)
        e1.saldo_de_gols+=resultado_e1
        e2.saldo_de_gols+=resultado_e2
        self.gols_e1=resultado_e1
        self.gols_e2=resultado_e2
        if resultado_e1 > resultado_e2:
            self.vencedor=self.equipe1
            e1._add_pontos(2)

        elif resultado_e1 < resultado_e2:
            self.vencedor= self.equipe2
            e2._add_pontos(2)

        elif resultado_e1 == resultado_e2:
            self.gols_e1=resultado_e1
            self.gols_e2=resultado_e2
            e1._add_pontos(1)
            e2._add_pontos(1)
        

    def mostrar_placar(self):
        return f'1 - {self.equipe1.nome} x 2 - {self.equipe2.nome}|| {self.gols_e1} x {self.gols_e2}'

    def mostrar_vencedor(self):
        if self.vencedor == None:
            print(f'essa partida ainda não tem vencedor')
        else:
            print(f'O vencedor da partida foi {self.vencedor}')
    
    @classmethod
    def find_partida(cls):
        pass