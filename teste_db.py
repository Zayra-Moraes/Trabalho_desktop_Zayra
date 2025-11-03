from package.models.Jogador_e_Tecnico import Jogador,Tecnico
from package.models.Equipe import Equipe
from package.controllers.serialjson import DataRecord

#j1=Jogador("Maria", 20, "centro", 123456789012)
#j2=Jogador('gabriel',21,"ponta", 1234567890)
t1=Tecnico('firmino',44,1234567890,123456)
#j3=Jogador('Zayra',22, 'linda', 1234567)
Tecnico.listar_tecnicos_cadastrados()
Jogador.listar_jogadores_cadastrados()
# g=Jogador.find_jogador('gabriel')
# g.atualizar_posicao('goleiro')
# g.atualizar_cpf(12345)
# j3.excluir_jogador()
# Jogador.listar_jogadores_cadastrados()

f=Equipe.find_equipe('flamengo')
f.mostrar_equipe()
# f.add_jogador('gabriel')
# f.mostrar_equipe()
# Jogador.listar_jogadores_cadastrados()

Equipe.listar_equipes_cadastradas()