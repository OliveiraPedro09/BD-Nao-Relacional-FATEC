from database import usuarios_collection, ObjectId

def favoritar_produto():
    usuario_id = input("Digite o ID do usuário: ")
    produto_id = input("Digite o ID do produto a ser favoritado: ")
    if usuario_id == '' or produto_id == '':
        print("ID do usuário e do produto são obrigatórios!")
        return
    usuarios_collection.update_one(
        {'_id': ObjectId(usuario_id)},
        {'$addToSet': {'favoritos': produto_id}}
    )
    print(f"Produto {produto_id} favoritado pelo usuário {usuario_id}.")