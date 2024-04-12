import psycopg2

def test_connection():
    try:
        # Estabelece a conexão com o banco de dados
        conn = psycopg2.connect(
            dbname='propriedades',
            user='postgres',
            password='1235',
            host='localhost',
            port='5432'
        )
        # Se a conexão for bem-sucedida, retorna True
        return True
    except psycopg2.Error as e:
        # Se ocorrer um erro, imprime o erro e retorna False
        print("Erro ao conectar ao banco de dados:", e)
        return False

# exemplo de consulta 

"""
import psycopg2

# Configuração da conexão com o banco de dados
conn = psycopg2.connect(
    dbname='nome_do_banco_de_dados',
    user='seu_nome_de_usuario',
    password='sua_senha',
    host='localhost',
    port='5432'
)
"""