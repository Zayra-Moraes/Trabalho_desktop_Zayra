from bottle import template

from package.models.Campeonato import Campeonato
from package.models.Equipe import Equipe
from package.models.Jogador_e_Tecnico import Jogador, Tecnico


class Application():
    def __init__(self):
        self.pages= {
            'home_page' :self.home_page,
            'equipes' : self.equipes,
            'atletas': self.atletas,
            'tecnicos': self.tecnicos,
            'login': self.login,
            'cadastro': self.cadastro
        }

    def render(self, page):
        content = self.pages.get(page)
        return content()

    def home_page(self):
        campeonatos=Campeonato.todos_os_campeonatos
        return template('home_page', campeonatos=campeonatos)

    def equipes(self):
        equipe=Equipe.todas_equipes_incritas
        return template('equipes', equipe=equipe)

    def atletas(self):
        jogadores=Jogador.todos_os_jogadores_inscritos
        return template('atletas', jogadores=jogadores)

    def tecnicos(self):
        tecnicos=Tecnico.todos_os_tecnicos_incritos
        return template('tecnicos', tecnicos=tecnicos)

    def login(self):
        return template('login')

    def cadastro(self):
        return template('cadastro')