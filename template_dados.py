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


# e=EquipeCampeonato.find_equipe_campeonato('Santos','Champions')
# print(e)

# ==============================
# EQUIPE 3 - PALMEIRAS
# ==============================
# j1 = Jogador("J1_Pal", 19, "ala", 333311111)
# j2 = Jogador("J2_Pal", 20, "ponta", 333311112)
# j3 = Jogador("J3_Pal", 21, "central", 333311113)
# j4 = Jogador("J4_Pal", 22, "pivô", 333311114)
# j5 = Jogador("J5_Pal", 23, "armador", 333311115)
# j6 = Jogador("J6_Pal", 24, "ala", 333311116)
# j7 = Jogador("J7_Pal", 25, "ala", 333311117)
# t3 = Tecnico("T3_Pal", 50, 555003, 900333333)
#
# palmeiras = Equipe("Palmeiras", 2025)
# for j in [j1, j2, j3, j4, j5, j6, j7]:
#     palmeiras.add_jogador(j)
# palmeiras.add_tecnico(t3)
#
#
# # ==============================
# # EQUIPE 4 - CORINTHIANS
# # ==============================
# j1 = Jogador("J1_Cor", 18, "ponta", 444411111)
# j2 = Jogador("J2_Cor", 19, "ala", 444411112)
# j3 = Jogador("J3_Cor", 20, "central", 444411113)
# j4 = Jogador("J4_Cor", 21, "pivô", 444411114)
# j5 = Jogador("J5_Cor", 22, "ala", 444411115)
# j6 = Jogador("J6_Cor", 23, "armador", 444411116)
# j7 = Jogador("J7_Cor", 24, "ala", 444411117)
# t4 = Tecnico("T4_Cor", 48, 555004, 900444444)
#
# corinthians = Equipe("Corinthians", 2024)
# for j in [j1, j2, j3, j4, j5, j6, j7]:
#     corinthians.add_jogador(j)
# corinthians.add_tecnico(t4)
#
#
# # ==============================
# # EQUIPE 5 - GRÊMIO
# # ==============================
# j1 = Jogador("J1_Gre", 20, "armador", 555511111)
# j2 = Jogador("J2_Gre", 21, "ponta", 555511112)
# j3 = Jogador("J3_Gre", 22, "ala", 555511113)
# j4 = Jogador("J4_Gre", 23, "central", 555511114)
# j5 = Jogador("J5_Gre", 24, "ala", 555511115)
# j6 = Jogador("J6_Gre", 25, "pivô", 555511116)
# j7 = Jogador("J7_Gre", 26, "ala", 555511117)
# t5 = Tecnico("T5_Gre", 52, 555005, 900555555)
#
# gremio = Equipe("Gremio", 2025)
# for j in [j1, j2, j3, j4, j5, j6, j7]:
#     gremio.add_jogador(j)
# gremio.add_tecnico(t5)
#
#
# # ==============================
# # EQUIPE 6 - VASCO
# # ==============================
# j1 = Jogador("J1_Vas", 19, "ponta", 666611111)
# j2 = Jogador("J2_Vas", 20, "ala", 666611112)
# j3 = Jogador("J3_Vas", 21, "central", 666611113)
# j4 = Jogador("J4_Vas", 22, "pivô", 666611114)
# j5 = Jogador("J5_Vas", 23, "armador", 666611115)
# j6 = Jogador("J6_Vas", 24, "ala", 666611116)
# j7 = Jogador("J7_Vas", 25, "ala", 666611117)
# t6 = Tecnico("T6_Vas", 49, 555006, 900666666)
#
# vasco = Equipe("Vasco", 2024)
# for j in [j1, j2, j3, j4, j5, j6, j7]:
#     vasco.add_jogador(j)
# vasco.add_tecnico(t6)
# c1=Campeonato('Champions')
c1=Campeonato.find_campeonato('Champions')
# c1.add_equipe('palmeiras')
# c1.add_equipe('corinthians')
# c1.add_equipe('gremio')
# c1.add_equipe('vasco')
# c1.add_equipe('santos')
# c1.add_equipe('flamengo')


# c1.criar_partida('palmeiras','corinthians','2x1')
# print(EquipeCampeonato.find_equipe_campeonato('corinthians','Champions'))
# c1.mostrar_equipes()
c2=Campeonato.find_campeonato('Final_fours')
c2.add_equipe('flamengo')
c2.add_equipe('palmeiras')
c2.criar_partida('palmeiras', 'flamengo','0x2')
#c2.tabela_de_posicoes()
# print(Equipe.find_equipe('flamengo'))
# c2.add_equipe('flamengo')
# c2.add_equipe('palmeiras')

#
# c2.criar_partida('palmeiras','flamengo','2x1')

