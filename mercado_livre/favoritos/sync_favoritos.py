from bson import ObjectId

def sync_favoritos(db_redis, favoritos_col):
    usuario_keys = db_redis.keys('usuario:*')
    
    for key in usuario_keys:
        usuario_id = key.decode('utf-8').split(':')[1]
        usuario_data = db_redis.hgetall(key)
        
        favoritos = {
            '_id': ObjectId(usuario_id),
            'favoritos': usuario_data.get(b'favoritos', b'[]').decode('utf-8')
        }
        
        favoritos_col.update_one({'_id': ObjectId(usuario_id)}, {'$set': favoritos}, upsert=True)
    
    print("Sincronização dos favoritos com o MongoDB realizada com sucesso!")