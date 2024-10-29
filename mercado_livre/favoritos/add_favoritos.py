from database_redis import createRedisDatabase
from bson import ObjectId

redis_client = createRedisDatabase()

def favorite_product():
    user_id = input("Digite o ID do usuário: ")
    product_id = input("Digite o ID do produto a ser favoritado: ")
    if user_id == '' or product_id == '':
        print("ID do usuário e do produto são obrigatórios!")
        return
    
    try:
        product_id = ObjectId(product_id)
    except Exception as e:
        print("ID do produto inválido!")
        return 
    
    if not redis_client:
        print("Erro de conexão com o banco de dados!")
        return
    
    user_key = f"usuario:{user_id}"
    user_data = redis_client.hgetall(user_key)
    
    if not user_data:
        print("Usuário não encontrado!")
        return
    
    favorite = user_data.get(b'favoritos', b'[]').decode('UTF-8')
    favorite_list = eval(favorite)
    favorite_list.append(str(product_id))

    redis_client.hset(user_key, "favoritos", str(favorite_list))
    print(f"Produto {product_id} favoritado pelo usuário {user_id}.")