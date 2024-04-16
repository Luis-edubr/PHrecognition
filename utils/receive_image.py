from db.connect_to_db import test_connection

def save_img_to_db(arquivo, conn):
    if conn:
        dados_imagem = arquivo.read()
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO images (dados) VALUES (%s)", (dados_imagem,))
            conn.commit()
        return 'Inserção realizada com sucesso'
    else:
        return 'Falha ao conectar ao banco de dados'


