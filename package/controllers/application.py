from bottle import template

from package.models.Campeonato import Campeonato


class Application():
    def __init__(self):
        self.pages= {
            'home_page' :self.home_page
        }

    def render(self, page):
        content = self.pages.get(page)
        return content()

    def home_page(self):
        campeonatos=Campeonato.todos_os_campeonatos
        return template('home_page', campeonatos=campeonatos)