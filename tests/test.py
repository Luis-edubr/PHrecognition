from db.connect_to_db import connect_to_db
from receive_image import save_img_to_db

def main():
    # Abrir o arquivo de imagem
    try:
        with open('C:/Users/luise/OneDrive/Imagens/5229311.jpg', 'rb') as arquivo_imagem:
            # Conectar ao banco de dados
            conn = connect_to_db()
            if conn:
                # Chamar a função para salvar a imagem no banco de dados
                resultado = save_img_to_db(arquivo_imagem, conn)
                print(resultado)
            else:
                print('Falha ao conectar ao banco de dados.')
    except FileNotFoundError:
        print('Arquivo de imagem não encontrado.')

if __name__ == '__main__':
    main()
