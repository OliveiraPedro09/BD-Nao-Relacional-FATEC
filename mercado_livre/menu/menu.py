from mercado_livre.compras.list_product import list_product
from mercado_livre.favoritos import sync_favoritos
from mercado_livre.favoritos.add_favoritos import favorite_product
from mercado_livre.favoritos.delete_favorite import delete_favorite
from mercado_livre.compras.buy_product import buy_product

def menu():
    while True:
        print("\n1. Gerenciar Usuários")
        print("2. Gerenciar Vendedores")
        print("3. Gerenciar Produtos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_favorite()
        elif opcao == '2':
            menu_purchase()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def menu_favorite():
    while True:
        print("\n1. Favoritar Produto")
        print("2. Deletar Favorito")
        print("3. Sincronizar Favoritos")
        print("4. Listar Favoritos")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            favorite_product()
        elif opcao == '2':
            delete_favorite()
        elif opcao == '3':
            sync_favoritos()
        elif opcao == '4':
            break
        elif opcao == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")

def menu_purchase():
    while True:
        print("\n1. Comprar Produto")
        print("2. Listar Compras")
        print("3. Sincronizar Compras")
        print("4. Listar Produtos")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            buy_product()
        elif opcao == '2':
            list_product()
        elif opcao == '3':
            sync_purchase()
        elif opcao == '4':
            list_product()
        elif opcao == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")