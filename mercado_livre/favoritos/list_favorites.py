def list_favorite(redis_client):
    favorite_keys = redis_client.keys('usuario:*:favoritos')

    for key in favorite_keys:
        favorite = redis_client.hgetall(key)
        favorite_id = key.decode('utf-8').split(':')[1]
        print(f"ID: {favorite_id}, Favoritos: {favorite}")