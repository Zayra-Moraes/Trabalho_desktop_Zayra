from package.controllers.serialjson import DataRecord

class EquipeCampeonato():
    db=DataRecord('equipe_campeonato.json')
    todas_EquipesCampeonatos=[]
    def __init__(self,equipe,campeonato,pontos=0,saldo_de_gols=0,from_dict= False,**kwargs):
        self.nome=equipe
        self.campeonato=campeonato
        self.pontos=kwargs.get('pontos',pontos)
        self.saldo_de_gols=kwargs.get('saldo_de_gols', saldo_de_gols)
        existente = EquipeCampeonato.find_equipe_campeonato(equipe, campeonato)

        if existente is None:
            EquipeCampeonato.todas_EquipesCampeonatos.append(self)
            if not from_dict:
                EquipeCampeonato.db.add(self)

    @classmethod
    def from_dict(cls):
        for data in cls.db.get_all():
            equipe=data.get('nome')
            campeonato=data.get('campeonato')
            pontos=data.get('pontos')
            saldo_de_gols=data.get('saldo_de_gols')
            self=EquipeCampeonato(equipe,campeonato,pontos,saldo_de_gols,from_dict=True)


    @classmethod
    def find_equipe_campeonato(cls,equipe,campeonato):
        for e in cls.todas_EquipesCampeonatos:
            if e.nome==equipe and e.campeonato==campeonato:
                return e
        return None

    def _add_pontos(self,pontos):
        self.pontos+=pontos
        EquipeCampeonato.db.update(self)

    def _add_saldo_de_gols(self,saldo_de_gols):
        self.saldo_de_gols+=saldo_de_gols
        EquipeCampeonato.db.update(self)

EquipeCampeonato.from_dict()