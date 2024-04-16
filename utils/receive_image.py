import os

def save_img_to_db(arquivo_ou_caminho, conn):
    if conn:
        if isinstance(arquivo_ou_caminho, str):  # Verifica se é um caminho para o arquivo
            # Abre o arquivo em modo de leitura binária ('rb')
            with open(arquivo_ou_caminho, 'rb') as arquivo:
                dados_imagem = arquivo.read()
        else:
            # Usa o objeto de arquivo aberto diretamente
            dados_imagem = arquivo_ou_caminho.read()

        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO images (dados) VALUES (%s)", (dados_imagem,))
            conn.commit()
        return 'Inserção realizada com sucesso'
    else:
        return 'Falha ao conectar ao banco de dados'
