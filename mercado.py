from typing import List, Dict
from time import sleep
from models.produto import Produto
from utils.helper import formata_float_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = [] # Carrinho é uma lista de produtos e quantidade do produto. No caso o Dicionario (Produto, quantidade)


def main() -> None:
    menu()


def menu() -> None:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('=-=-=-=-=-=-=-==-=-=-=- FOX SHOPy -=-=-==-=-=-=-=-=-=-=')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

    print('Selecione uma opção abaixo:\n')
    print('   1 - Cadastrar Produto.')
    print('   2 - Listar Produto.')
    print('   3 - Comprar Produto.')
    print('   4 - Visualizar Carrinho.')
    print('   5 - Fechar Pedido.')
    print('   6 - Sair do Sistema.')

    opcao: int = int(input('Informe o que deseja fazer: '))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        print('\n\n')
        listar_produto()
    elif opcao == 3:
        print('\n\n')
        comprar_produto()
    elif opcao == 4:
        print('\n\n')
        visualizar_carrinho()
    elif opcao == 5:
        print('\n\n')
        fechar_pedido()
    elif opcao == 6:
        print('\n\n')
        print('Volte sempre!!!')
        sleep(2)
        exit(0)
    else:
        print('\n\n')
        print('Opção Invalida, tente novamente!')
        menu()


def cadastrar_produto() -> None:
    print('\n\n')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    nome: str = str(input('Informe o nome do Produto: '))
    try:
        preco: float = float(input('Informe o valor do Produto: '))
    except:
        print('\n')
        print('   ERROR! O valor informado deve ser numeros!')
        print('\n\n')
        sleep(2)
        menu()

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produto() -> None:
    if len(produtos) > 0:
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Listagem de produtos:')
        for produto in produtos:
            print(produto)
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            sleep(1)

    else:
        print('Ainda não existe produtos cadastrados.')
    sleep(2)
    print('\n\n')
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o produto que deseja adicionar no carrinho:\n')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('=-=-=-=-=-=- Produtos Disponiveis -=-=-=-=-=-=')
        for produto in produtos:
            print(produto)
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            sleep(1)

        try:
            codigo: int = int(input('Informe o Código do produto: '))
        except:
            print('    ERROR! - Informe o numero.')
            sleep(2)
            print('\n\n')
            comprar_produto()

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto) # .get(chave) = pega o valor da chave que é o produto.
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} possui {item[produto]} unidade em carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado no carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1} # item = Item de um produto.
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com {codigo} não foi encontrado.')
            sleep(2)
            menu()

    else:
        print('Ainda não existe produtos para vender.')
        sleep(2)
        menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(f'Produto: {dados[0]} Quantidade: {dados[1]}')
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    else:
        print('Ainda nao existe produto no carrinho.')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do Carrinho: ')
        for item in carrinho:
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            for dados in item.items():
                print(f'{dados[0]}') # dados[0] = Produto
                print(f'     Quantidade: {dados[1]}') # dados[1] = Quantidade do produto
                valor_total += dados[0].preco * dados[1]
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte Sempre')
        carrinho.clear()
        sleep(5)

    else:
        print('Ainda nao existe produtos no carrinho!')
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()