def list_product(redis_client):
    produto_keys = redis_client.keys('produto:*')
    
    for key in produto_keys:
        product = redis_client.hgetall(key)
        product_id = key.decode('utf-8').split(':')[1]
        name = product.get(b'nome', b'').decode('utf-8')
        price = product.get(b'preco', b'').decode('utf-8')
        print(f"ID: {product_id}, Nome: {name}, Preço: {price}")