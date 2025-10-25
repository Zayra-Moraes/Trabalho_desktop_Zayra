from package.models.Equipe import Equipe
from package.models.Campeonato import Campeonato
from package.controllers.Menu_cadastro import Menu_cadastro
from package.controllers.Menu_jogador_tecnico import Menu_jogador_tecnico
from package.controllers.Menu_equipe import Menu_equipe
from package.utils.Functions import validador_int,cabecalho,menu,linha


class Gerenciador():
    def __init__(self):
        self.opcoes= {
            "1": self.area_cadastro,
            "2": self.area_jogador_tecnico,
            "3": self.area_equipe,
            "4": self.area_campeonato,
            "0": self.sair
        }
        self.executando=True

    def executar(self):
        while self.executando:
            cabecalho('gerenciador de campeonato')
            menu(['area de cadastro','area do jogador e técnico', 'area da equipe', 'area do campeonato'])
            opc=input('Digite sua opção:')
            entrar=self.opcoes.get(opc)
            if entrar:
                entrar()
            else:
                print('Por favor digite uma das opcões')

#Menu principal:
    def area_cadastro(self):
        while True:
            cabecalho('área de cadastro no sistema')
            menu(['cadastrar jogador', 'cadastrar tecnico', 'cadastrar equipe', 'cadastrar campeonato', 'exluir algum cadastro'])
            print(f'Escolha o que você deseja cadastrar:')
            opcoes_cadastro={
                "1" : Menu_cadastro.jogador,
                "2" : Menu_cadastro.tecnico,
                "3" : Menu_cadastro.equipe,
                "4" : Menu_cadastro.campeonato,
                "5" : Menu_cadastro.excluir_algum_cadastro,
                "0" : self.voltar
            }
            linha()
            opc=input('Digite sua Opção:')
            if opc == "0":
                break
            entrar=opcoes_cadastro.get(opc)
            if entrar:
                entrar()
            else:
                print(f'opção inválida')

    def area_jogador_tecnico(self):
        while True:
            cabecalho('área de informações dos Jogador e Técnico')
            menu(['mostrar jogadores ou técnicos cadastrados', 'Buscar jogador ou técnico', 'Atualizar Dados'])
            opcoes_jogador={
                "1" : Menu_jogador_tecnico.mostrar,
                "2" : Menu_jogador_tecnico.buscar,
                "3" : Menu_jogador_tecnico.atualizar,
                "0" : self.voltar
                }
            linha()
            opc=input('Digite sua opção:')
            entrar=opcoes_jogador.get(opc)
            if opc == '0':
                break
            if entrar:
                entrar()
            else:
                print('Opção inválida.')
            
    def area_equipe(self):
        while True:
            cabecalho('área de informações das equipes cadastradas')
            opcoes={
                "1" : Menu_equipe.dados,
                "2" : Menu_equipe.add,
                "3" : Menu_equipe.remove,
                "0" : self.voltar
            }
            Equipe.listar_equipes_cadastradas()
            print(linha())
            menu(['Mais dados da equipe (pontos, saldo de gols, integrantes)', 'Adicionar um técnico ou jogador', 'Remover um técnico ou jogador'])
            opc=input('Digite sua opção:')
            entrar=opcoes.get(opc)
            if opc == "0":
                break
            if entrar:
                entrar()
            else:
                print('Opção inválida')

    def area_campeonato(self):
        while True:
            cabecalho('área de informações dos campeonatos inscritos')
            opcoes={
                "1" : self.add_equipes,
                "2" : self.mostrar_equipes,
                "3" : self.criar_partidas,
                "4" : self.mostrar_partidas,
                "5" : self.tabela_de_classificacao
            }
            Campeonato.listar_todos_campeonatos()
            print(linha())
            menu(['Adicionar mais equipes em um campeonato', 'Mostrar as equipes inscritas no campeonato', 'Criar mais partidas em um campeonato', 'Mostrar partidas finalizadas', 'Tabela de classificação de campeonato'])
            opc=input('Digite sua opção:')
            entrar=opcoes.get(opc)
            if opc == "0":
                break
            if entrar:
                entrar()
            else:
                print('Opção inválida')

    def sair(self):
        print(f'Saindo do sistema...')
        self.executando=False

    def voltar(self):
        return f'voltar'

#Menu de gerenciamento de campeonato
    def add_equipes(self):
        n_campeonato=validador_int('Digite o número do campeonato que deseja adicionar mais equipes:')
        Equipe.listar_equipes_cadastradas()
        n_equipe=input('Digite o NOME da equipe que deseja adicionar no campeonato:')
        e=Equipe.find_equipe(n_equipe)
        if e:
            Campeonato.todos_os_campeonatos[n_campeonato-1].add_equipe(e)
            Campeonato.todos_os_campeonatos[n_campeonato-1].mostrar_equipes()
        else:
            print(f'Nenhuma equipe com esse nome encontrada')

    def mostrar_equipes(self):
        n_campeonato=validador_int('Digite o número do campeonato que você deseja ver as equipes:')
        Campeonato.todos_os_campeonatos[n_campeonato-1].mostrar_equipes()
        
    def criar_partidas(self):
        n_campeonato=validador_int('Digite o número do campeonato que você deseja criar partidas:')
        c=Campeonato.todos_os_campeonatos[n_campeonato-1]
        c.mostrar_equipes()
        while True:
            e1=input('NOME da equipe 1:')
            e2=input('NOME da equipe 2:')
            e_1=Equipe.find_equipe(e1)
            e_2=Equipe.find_equipe(e2)
            if e_1 and e_2:
                placar=input(f"Por favor inserir o placar final da partida: (no formato '2x1')")
                c.criar_partida(e_1,e_2,placar)
                break
            else:
                print('Alguma equipe não encontrada')

    def mostrar_partidas(self):
        n_campeonato=validador_int('Digite o número do campeonato que deseja ver as partidas:')
        Campeonato.todos_os_campeonatos[n_campeonato-1].mostrar_partidas()

    def tabela_de_classificacao(self):
        n_campeonato=validador_int('Digite o número do campeonato que deseja ver a tabela de classificação:')
        Campeonato.todos_os_campeonatos[n_campeonato-1].tabela_de_classificacao()