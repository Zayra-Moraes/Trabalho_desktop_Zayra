from package.controllers.Gerenciador import Gerenciador
from test_Partida_e_Campeonato import teste

def workspace():
    teste.workspace()
    app=Gerenciador()
    app.executar()

if __name__ == '__main__':
    workspace()