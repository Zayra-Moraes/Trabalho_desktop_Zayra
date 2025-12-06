from package.models.Jogador_e_Tecnico import Jogador,Tecnico
from package.models.Equipe import Equipe
from package.models.Campeonato import Campeonato
from package.utils.Functions import validador_int,menu,cabecalho

class Menu_cadastro:
    @staticmethod
    def jogador():
        nome=input('Digite o nome do Jogador:')
        idade=validador_int('Digite a idade do Jogador:')
        posicao=input('Digite a posicao do jogador:')
        cpf=validador_int('Digite o cpf do jogador:')
        j=Jogador(nome, idade, posicao, cpf)
        print(F'O jogador {j.nome} foi cadastrado com sucesso.')

    @staticmethod
    def tecnico():
        nome=input('Digite o nome do tecnico:')
        idade=validador_int('Digite a idade do tecnico:')
        licenca=validador_int('Digite a licença do tecnico:')
        cpf=validador_int('Digite o cpf do tecnico:')
        t=Tecnico(nome, idade, licenca, cpf)
        print(F'O tecnico {t.nome} foi cadastrado com sucesso.')

    @staticmethod
    def equipe():
        nome=input('Digite o nome da equipe que você deseja cadastrar:')
        ano=validador_int('Digite o ano de criação da sua equipe:')
        e=Equipe(nome,ano)
        print(f'A equipe {e.nome} foi cadastrada com sucesso.')

    @staticmethod
    def campeonato():
        nome=input('Digite o nome do campeonato:')
        c=Campeonato(nome)
        print(f'O campeonato {c.nome} foi cadastrada com sucesso.')

    @staticmethod
    def excluir_algum_cadastro():
        cabecalho('O que você deseja excluir?')
        menu(['jogador', 'tecnico', 'equipe', 'campeonato' ])
        while True:
            opc=int(input('Digite uma opção:'))
            if opc == 0:
                break
            elif opc == 1:
                nome=input('Digite o nome do jogador:')
                jogador=Jogador.find_jogador(nome)
                if jogador:
                    print(jogador.dados_completos())
                    menu(['sim', 'não'])
                    ctz=int(input('Realmente deseja excluir?'))
                    if ctz == 1:
                        jogador.excluir_jogador()
                        print(f'Jogador excluido do sistema')
                        break
                    elif ctz == 2 or ctz == 0:
                        break
                    else:
                        print(f'Opção inválida')
                else:
                    print(f'Nenhum jogador com esse nome encontrado.')

            elif opc == 2:
                nome=input('Digite o nome do tecnico:')
                tecnico=Tecnico.find_tecnico(nome)
                if tecnico:
                    print(tecnico.dados_completos())
                    menu(['sim', 'não'])
                    ctz=int(input('Realmente deseja excluir?'))
                    if ctz == 1:
                        tecnico.excluir_tecnico()
                        print(f'Técnico excluido do sistema')
                        break
                    elif ctz == 2 or ctz == 0:
                        break
                    else:
                        print(f'Opção inválida')   
                else:
                    print(f'Nenhum técnico com esse nome encontrado.') 
                        
            elif opc == 3:
                nome=input('Digite o nome do equipe:')
                equipe=Equipe.find_equipe(nome)
                if equipe:
                    equipe.mostrar_equipe()
                    menu(['sim', 'não'])
                    ctz=int(input('Realmente deseja excluir?'))
                    if ctz == 1:
                        equipe.exluir_equipe()
                        print(f'Equipe excluida do sistema')
                        break
                    elif ctz == 2 or ctz == 0:
                        break
                    else:
                        print(f'Opção inválida')
                else: 
                    print(f'Nenhuma equipe com esse nome encontrada.')   

            elif opc == 4:
                nome=input('Digite o nome do Campeonato:')
                campeonato=Campeonato.find_campeonato(nome)
                if campeonato:
                    print(f'Campeonato encontrado.')
                    menu(['sim', 'não'])
                    ctz=int(input('Realmente deseja excluir?'))
                    if ctz == 1:
                        campeonato.excluir_campeonato()
                        print(f'Campeonato excluido do sistema.')
                        break
                    elif ctz == 2 or ctz == 0:
                        break
                    else:
                        print(f'Opção inválida')   
                else:
                    print(f'Nenhum campeonato com esse nome encontrado.')
            else: 
                print('Por favor digite uma das opcões:')

