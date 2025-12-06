from bottle import Bottle,run,request,response,static_file
from bottle import template

from package.controllers.application import Application
from package.models.Campeonato import Campeonato

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
    partidas=campeonato.partidas
    classificacao=campeonato.tabela_de_posicoes()
    return template('campeonato',campeonato=campeonato,partidas=partidas,classificacao=classificacao)


run(app, host='127.0.0.1', port=8080, debug=True,reloader=True)

# @app.route('/')
# def home(): return template("home_page")
#
# run(app,host='127.0.0.1',port=8080,debug=True)