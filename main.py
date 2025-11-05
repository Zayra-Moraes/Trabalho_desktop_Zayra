from package.controllers.Gerenciador import Gerenciador

def workspace():
    app=Gerenciador()
    app.executar()

if __name__ == '__main__':
    workspace()