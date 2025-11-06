from package.controllers.serialjson import DataRecord
class Partida():
    contador=0
    todas_as_partidas=[]    
    db=DataRecord('partidas.json')
    def __init__(self, equipe1, equipe2,gols_e1=0,gols_e2=0, vencedor=None,from_json=False,**kwargs):
        Partida.contador+=1
        self.id=Partida.contador
        self.equipe1=equipe1
        self.equipe2=equipe2
        self.vencedor=kwargs.get('vencedor') or vencedor
        self.gols_e1=kwargs.get('gols_e1') or gols_e1
        self.gols_e2=kwargs.get('gols_e2') or gols_e2
        if self not in Partida.todas_as_partidas:
            Partida.todas_as_partidas.append(self)
        if not from_json:
            Partida.db.add(self)

    @classmethod
    def save_partida(cls):
        pass

    def to_dict(self):
        return {
            "id": self.id,
        }

    @classmethod
    def carregar_todos(cls):
        cls.todas_as_partidas=[]
        for data in cls.db.get_all():
            equipe1 = data.get('equipe1')
            equipe2 = data.get('equipe2')
            gols_e1 = data.get('gols_e1')
            gols_e2 = data.get('gols_e2')
            vencedor = data.get('vencedor')
            partida=cls(equipe1, equipe2, gols_e1, gols_e2, vencedor,from_json=True)
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
            vencedor = self.equipe1
            self.vencedor=vencedor
            e1._add_pontos(2)

        elif resultado_e1 < resultado_e2:
            vencedor=self.equipe2
            self.vencedor= vencedor
            e2._add_pontos(2)

        elif resultado_e1 == resultado_e2:
            self.gols_e1=resultado_e1
            self.gols_e2=resultado_e2
            e1._add_pontos(1)
            e2._add_pontos(1)
            self.vencedor='empate'

        self.db.update_por_id(self)
        

    def mostrar_placar(self):

        return f'{self.equipe1} X {self.equipe2} || {self.gols_e1} x {self.gols_e2}'

    def mostrar_vencedor(self):
        if self.vencedor == None:
            print(f'essa partida ainda não tem vencedor')
        else:
            print(f'O vencedor da partida foi {self.vencedor}')
    
    @classmethod
    def find_partida(cls,id):
        for p in cls.todas_as_partidas:
            if p.id == id:
                return p
        return None

Partida.carregar_todos()