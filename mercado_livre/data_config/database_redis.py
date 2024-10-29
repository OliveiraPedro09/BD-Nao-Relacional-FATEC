import redis

def createRedisDatabase():
    try:
        connect = redis.Redis(
            host='redis-18915.c308.sa-east-1-1.ec2.redns.redis-cloud.com',
            port=18915,
            password='MV64eb0W0SUwjPccj09JFkcyDyIL86Xg'
        )
        connect.ping()
        print('Conectado com sucesso ao Redis!')
        return connect
    except redis.ConnectionError:
        print('Erro de conexão com o Redis!')
        return None