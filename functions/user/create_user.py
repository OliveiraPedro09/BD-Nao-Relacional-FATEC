def create_user(session, name, email, cpf, password):
    script = """
    CREATE (u:User {
        name: $name,
        email: $email,
        cpf: $cpf,
        password: $password
    })
    RETURN elementId(u) as id
    """
    result = session.run(script, name=name, email=email, cpf=cpf, password=password)
    user_id = result.single()["user_id"]
    return user_id
