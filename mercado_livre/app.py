from mercado_livre.data_config.database_mongo import createMongoDatabase
from mercado_livre.data_config.database_redis import createRedisDatabase
from mercado_livre.auth import login, user_logged
from mercado_livre.menu import menu

def main():
    db_mongo = createMongoDatabase()
    db_redis = createRedisDatabase()

    if db_mongo is None or db_redis is None:
        print("Erro ao conectar aos bancos de dados!")
        return
    
    usuarios_collection = db_mongo['Usuario']
    produtos_collection = db_mongo['Produtos']
    compras_collection = db_mongo['Compras']

    user_email = input("Digite o email do usuário: ")
    user_password = input("Digite a senha do usuário: ")

    user = login(usuarios_collection, db_redis, user_email, user_password)
    if user is None:
        print("Usuário não encontrado!")
        return

    print("Usuário autenticado com sucesso! Bem-Vindo!")
    menu(db_mongo, db_redis, user)

if __name__ == "__main__":
    main()