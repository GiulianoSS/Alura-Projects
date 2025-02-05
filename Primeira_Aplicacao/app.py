import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa','ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza','ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano','ativo':False}]

def exibir_nome_do_programa():
    print("""
    ⟆Ꭿᑲ𝖮ᖇ ᕮⲭᕈᖇ∈⟆⟆
    """)

def exibir_opcoes():
    print('1. Cadastra Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando app')

def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')
    voltar_menu()

def alternar_estado():
    exibir_subtitulo('Alterando estado do restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
   

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')


    voltar_menu()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
            #print('Cadastrar restaurante')
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()