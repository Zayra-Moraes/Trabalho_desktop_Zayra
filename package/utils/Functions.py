def linha():
    n=40
    return f'-'*n
    
def cabecalho(titulo):
    print(linha())
    print(titulo.upper().center(40))
    print(linha())

def menu(lista):
    n=1
    for i in lista:
        print(f'{n} - {i.capitalize()}')
        n+=1
    print(f'0 - Sair')
    print(linha())

def validador_int(m):
        print(m)
        while True:
            valor=input()
            if valor.isdigit():
                return int(valor)
            print(f'Por favor digite apenas números')