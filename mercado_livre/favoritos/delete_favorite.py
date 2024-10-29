from bson import ObjectId
from database_redis import createRedisDatabase

redis_client = createRedisDatabase()

def delete_favorite():
    user_id = input("Digite o ID do usuário: ")
    product_id = input("Digite o ID do produto a ser desfavoritado: ")

    if user_id == '' or product_id == '':
        print("ID do usuário e do produto são obrigatórios!")
        return
    
    try:
        product_id = ObjectId(product_id)
    except Exception as e:
        print("ID do produto inválido!")
        return
    
    if not redis_client:
        print("Erro ao conectar ao Redis!")
        return
    
    user_key = f"usuario:{user_id}"
    user_data = redis_client.hgetall(user_key)
    
    if not user_data:
        print("Usuário não encontrado!")
        return

    favorite = user_data.get(b'favoritos', b'[]').decode('utf-8')
    favorite_list = eval(favorite)

    if str(product_id) in favorite_list:
        favorite_list.remove(str(product_id))
    else:
        print("Produto não encontrado nos favoritos do usuário!")
        return

    redis_client.hset(user_key, "favoritos", str(favorite_list))
    print(f"Produto {product_id} desfavoritado pelo usuário {user_id}.")