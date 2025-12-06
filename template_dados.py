from package.models.Campeonato import Campeonato
from package.models.EquipeCampeonato import EquipeCampeonato
from package.models.Partida import Partida
from package.models.Jogador_e_Tecnico import Jogador,Tecnico
from package.models.Equipe import Equipe
class teste():
    def workspace():

        #Uma partida só pode ser definida (seu placar ou vencedor), se ela for iniciada primeiramente dentro de um campeonato
        #Então vamos criar um campeonato:
        # champions=Campeonato('Champions')
        Final_fours=Campeonato('Final_fours')
        libertadores=Campeonato('Libertadores')
        #Para que suas funções funcionem corretamente devemos adicionar as equipes e seus jogadores
        #pois as equipes só podem fazer parte do campeonato se tiverem no mínimo 7 jogadores cadastrados
        # zayra=Jogador('Zayra',19,'central',394823084)
        # gabriel=Jogador('Gabriel',20,'ponta',3827490)
        # p3=Jogador('p3',20, 'central',938724894)
        # p4=Jogador('p4',20, 'central', 39493443)
        # p5=Jogador('p5',23, 'central', 3425455)
        # p6=Jogador('p6',33, 'central', 8957485)
        # p7=Jogador('p7', 22, 'central', 34245325)
        # t2=Tecnico('t1',43,43244,2345678901)
        #
        # mary=Jogador('Mary', 19, 'ponta',39248094)
        # dani=Jogador('Dani',19, 'armação',3904824)
        # p8=Jogador('p8', 22, 'central', 34245325)
        # p9=Jogador('p9', 22, 'central', 34245325)
        # p10=Jogador('p10', 22, 'central', 34245325)
        # p11=Jogador('p11', 22, 'central', 34245325)
        # p12=Jogador('p12', 22, 'central', 34245325)
        # p13=Jogador('p13', 22, 'central', 34245325)
        # t1=Tecnico('t2', 42, 34890,897822349)
        #
        # flamengo=Equipe('flamengo', 2025 )
        # Santos=Equipe('santos', 2024)
        #
        # flamengo.add_jogador(zayra)
        # flamengo.add_jogador(gabriel)
        # flamengo.add_jogador(p3)
        # flamengo.add_jogador(p4)
        # flamengo.add_jogador(p5)
        # flamengo.add_jogador(p6)
        # flamengo.add_jogador(p7)
        # flamengo.add_tecnico(t1)
        #
        #
        # Santos.add_jogador(mary)
        # Santos.add_jogador(dani)
        # Santos.add_jogador(p8)
        # Santos.add_jogador(p9)
        # Santos.add_jogador(p10)
        # Santos.add_jogador(p11)
        # Santos.add_jogador(p12)
        # Santos.add_jogador(p13)
        # Santos.add_tecnico(t2)
        #
        #
        # #adicionar equipes no campeonato:
        # champions.add_equipe('flamengo')
        # champions.add_equipe('Santos')
#        champions.mostrar_equipes()
        #Aqui vai precisar de um input para o placar da partida, que posteriormente vai se comunicar com o menu
        #como apenas estamos testando a função, agora ela é um input
#        champions.criar_partida(flamengo,Santos)
        #Por favor digitar um input para continuar o código
#        champions.mostrar_partidas()
#        champions.tabela_de_classificacao()

c1=Campeonato.find_campeonato('Champions')
# c1.add_equipe('Santos')
c1.mostrar_equipes()
# e=EquipeCampeonato.find_equipe_campeonato('Santos','Champions')
# print(e)
c1.criar_partida('flamengo','Santos','2x6')

