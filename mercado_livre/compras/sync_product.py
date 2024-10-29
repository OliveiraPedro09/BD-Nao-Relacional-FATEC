from bson import ObjectId

def sync_produtos(db_redis, produtos_col):
    produto_keys = db_redis.keys('produto:*')
    
    for key in produto_keys:
        produto_id = key.decode('utf-8').split(':')[1]
        produto_data = db_redis.hgetall(key)
        
        produto = {
            '_id': ObjectId(produto_id),
            'nome': produto_data.get(b'nome', b'').decode('utf-8'),
            'preco': float(produto_data.get(b'preco', b'0').decode('utf-8'))
        }
        
        produtos_col.update_one({'_id': ObjectId(produto_id)}, {'$set': produto}, upsert=True)
    
    print("Sincronização dos produtos com o MongoDB realizada com sucesso!")