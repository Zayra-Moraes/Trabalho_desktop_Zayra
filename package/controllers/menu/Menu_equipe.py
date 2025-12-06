from package.models.Equipe import Equipe
from package.models.Jogador_e_Tecnico import Jogador,Tecnico
from package.utils.Functions import validador_int,menu,cabecalho,linha

class Menu_equipe:
    @staticmethod
    def dados():
        n_equipe=validador_int('Digite o número da equipe que você deseja mostrar mais dados:')
        Equipe.todas_equipes_incritas[n_equipe-1].mostrar_pontos()
        Equipe.todas_equipes_incritas[n_equipe-1].mostrar_saldo_de_gols()
        Equipe.todas_equipes_incritas[n_equipe-1].mostrar_equipe()

    @staticmethod
    def add():
        while True:
            equipe=validador_int('Digite o número da equipe que deseja adicionar:')
            cabecalho('O que quer adicionar?')
            menu(['Jogadores', 'Técnico'])
            opc=validador_int('Digite uma opção:')
            if opc == 1:
                Jogador.listar_jogadores_cadastrados()
                print(linha())
                nome_j=input('Digite o nome do jogador que você deseja adicionar:')
                j=Jogador.find_jogador(nome_j)
                if j:
                    print(j.dados_completos()) 
                    Equipe.todas_equipes_incritas[equipe-1].add_jogador(j)
                    break
                else:
                    print('Nome digitado incorretamente')
                
            elif opc ==2:
                Tecnico.listar_tecnicos_cadastrados()
                print(linha())
                nome_t=input('Digite o nome do técnico que você deseja adicionar:')
                t=Tecnico.find_tecnico(nome_t)
                if t:
                    print(t.dados_completos())
                    Equipe.todas_equipes_incritas[equipe-1].add_tecnico(t)
                    break
                else:
                    print(f'Nenhum jogador com esse nome cadastrado')

            elif opc == 0:
                break



    @staticmethod
    def remove():
        equipe=validador_int('Digite o número da equipe que deseja remover integrantes:')
        Equipe.todas_equipes_incritas[equipe-1].mostrar_equipe()
        cabecalho('O que quer remover?')
        menu(['Jogadores', 'Técnico'])
        while True:
            opc=validador_int('Digite uma opção:')
            if opc == 1:
                
                print(linha())
                nome_j=input('Digite o nome do jogador que você deseja remover:')
                j=Jogador.find_jogador(nome_j)
                if j:
                    print(j.dados_completos())
                    Equipe.todas_equipes_incritas[equipe-1].remover_jogador(j)
                    break
                else:
                    print('Nenhum jogador com esse nome encontrado')
            elif opc ==2:
                
                print(linha())
                nome_t=input('Digite o nome do técnico que você deseja remover:')
                t=Tecnico.find_tecnico(nome_t)
                if t:
                    print(t.dados_completos())
                    Equipe.todas_equipes_incritas[equipe-1].remover_tecnico(t)
                    break
                else: 
                    print('Nenhum jogador com esse nome encontrado.')

            elif opc == 0:
                break