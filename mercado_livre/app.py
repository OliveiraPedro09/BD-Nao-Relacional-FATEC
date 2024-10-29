import sys
import os

# Adicione o caminho do diretório onde 'database_mongo.py' está localizado
sys.path.append(os.path.join(os.path.dirname(__file__), 'mercado_livre', 'data_config'))

from database_mongo import createMongoDatabase
from database_redis import createRedisDatabase
from menu import menu
from auth import login, user_logged
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    db_mongo = createMongoDatabase()
    db_redis = createRedisDatabase()

    if db_mongo is None or db_redis is None:
        print("Erro ao conectar aos bancos de dados!")
        return
    
    usuarios_collection = db_mongo['Usuario']
    vendedores_collection = db_mongo['Vendedores']
    produtos_collection = db_mongo['Produtos']
    favoritos_collection = db_mongo['Favoritos']
    compras_collection = db_mongo['Compras']

    user_email = input("Digite o email do usuário: ")
    user_password = input("Digite a senha do usuário: ")

    user = login(usuarios_collection, db_redis, user_email, user_password)

    if user is None:
        print("Usuário não encontrado!")
        return
    
    print("Usuário autenticado com sucesso! Bem-Vindo !")

    while True:
        menu(db_mongo, db_redis, user);

if __name__ == "__main__":
    main()