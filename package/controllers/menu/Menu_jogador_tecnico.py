from package.models.Jogador_e_Tecnico import Jogador,Tecnico
from package.utils.Functions import menu,cabecalho

class Menu_jogador_tecnico:
    @staticmethod
    def mostrar():
        cabecalho('Deseja ver os jogadores ou técnicos cadastrados?')
        menu(['jogador', 'tecnico'])
        while True:
            opc=int(input('Digite uma opção:'))
            if opc == 0:
                break
            elif opc == 1:
                Jogador.listar_jogadores_cadastrados()
                break
            elif opc == 2:
                Tecnico.listar_tecnicos_cadastrados()
                break
            else:
                print('Por favor digite uma das opcões:')
    
    @staticmethod
    def buscar():
        nome=input('Digite o nome do jogador ou técnico que pretende buscar:')
        print('Jogador:')
        Jogador.find_jogador(nome)
        print(f'Técnico:')
        Tecnico.find_tecnico(nome)

    @staticmethod
    def atualizar():
        cabecalho('Deseja atualizar dados de jogadores ou técnicos cadastrados?')
        menu(['jogador', 'tecnico'])
        while True:
            opc=int(input('Digite uma opção:'))
            if opc == 0:
                break
            elif opc == 1:
                while True:
                    menu(['Idade', 'Posição'])
                    alterar=int(input('O que deseja alterar?'))
                    if alterar == 1:
                        nome=input('Digite o nome do jogador:')
                        jogador=Jogador.find_jogador(nome)
                        if jogador:
                            nova_idade=input('Digite a nova idade do jogador:')
                            jogador.atualizar_idade(nova_idade)
                            print(jogador.dados_completos())
                            break
                    elif alterar == 2:
                        nome=input('Digite o nome do jogador:')
                        jogador=Jogador.find_jogador(nome)
                        if jogador:
                            nova_pos=input('Digite a nova posição do jogador:')
                            jogador.atualizar_posicao(nova_pos)
                            print(jogador.dados_completos())

                    elif alterar == 0:
                        break

                    else: 
                        break

            elif opc ==2:
                while True:
                    nome=input('Digite o nome do técnico que você deseja mudar a idade: (digite 0 para voltar)')
                    if nome == 0:
                        break
                    tecnico=Tecnico.find_tecnico(nome)
                    if tecnico:
                        nova_idade=input('Digite a nova idade do técnico:')
                        tecnico.atualizar_idade(nova_idade)
                        print(tecnico.dados_completos())
                        break

            else:
                print('Por favor digite uma das opcões:')