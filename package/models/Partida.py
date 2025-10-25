class Partida():
    def __init__(self, equipe1, equipe2):
        self.equipe1=equipe1
        self.equipe2=equipe2
        self.vencedor=None
        self.gols_e1=0
        self.gols_e2=0

    
    def _definir_placar(self, resultado_e1, resultado_e2):
        self.equipe1.saldo_de_gols+=resultado_e1
        self.equipe2.saldo_de_gols+=resultado_e2
        self.gols_e1=resultado_e1
        self.gols_e2=resultado_e2
        if resultado_e1 > resultado_e2:
            self.vencedor=self.equipe1
            self.equipe1._add_pontos(2)

        elif resultado_e1 < resultado_e2:
            self.vencedor= self.equipe2
            self.equipe2._add_pontos(2)

        elif resultado_e1 == resultado_e2:
            self.gols_e1=resultado_e1
            self.gols_e2=resultado_e2
            self.equipe1._add_pontos(1)
            self.equipe2._add_pontos(1)
        

    def mostrar_placar(self):
        return f'1 - {self.equipe1.nome} x 2 - {self.equipe2.nome}|| {self.gols_e1} x {self.gols_e2}'

    def mostrar_vencedor(self):
        if self.vencedor == None:
            print(f'essa partida ainda não tem vencedor')
        else:
            print(f'O vencedor da partida foi {self.vencedor}')
    
