import redis

def createRedisDatabase():
    try :
        connect = redis.Redis(
            host = 'redis-18915.c308.sa-east-1-1.ec2.redns.redis-cloud.com',
            port =  18915,
            password = 'MV64eb0W0SUwjPccj09JFkcyDyIL86Xg'
            #Esses valores de cima serão mudados de acordo com o seu banco de dados
        )
        connect.ping()
        print('Conectado com sucesso ao Redis!')
        return connect
    except redis.ConnectionError:
        print('Erro de conexão com o Redis!')
        return None
    except Exception as e:
        print(f'Erro inesperado: {e}')
        return None
    



