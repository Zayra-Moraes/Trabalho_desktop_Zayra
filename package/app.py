from bottle import Bottle,run,request,response,static_file
from bottle import template

from package.controllers.application import Application
from package.models.Campeonato import Campeonato
from package.models.Partida import Partida

app=Bottle()
ctl=Application()

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


@app.route('/', method='GET')
def home(): return ctl.render('home_page')

@app.route('/campeonato/<nome>', method='GET')
def campeonato(nome):
    campeonato=Campeonato.find_campeonato(nome)
    partidas=[]
    for p in campeonato.partidas:
        partida=Partida.find_partida(p)
        if partida:
            partidas.append(partida.to_dict())
    classificacao=campeonato.tabela_de_posicoes()
    return template('campeonato',campeonato=campeonato,partidas=partidas,classificacao=classificacao)

@app.route('/equipes', method='GET')
def equipes(): return ctl.render('equipes')


@app.route('/cadastro/Atletas', method='GET')
def atletas(): return ctl.render('atletas')

@app.route('/cadastro/Técnicos', method='GET')
def tecnicos(): return ctl.render('tecnicos')

@app.route('/login', method='GET')
def login(): return ctl.render('login')

@app.route('/logout', method='GET')
def logout(): return ctl.render('logout')

@app.route('/cadastro',method='GET')
def cadastro(): return ctl.render('cadastro')

run(app, host='127.0.0.1', port=8080, debug=True,reloader=True)
