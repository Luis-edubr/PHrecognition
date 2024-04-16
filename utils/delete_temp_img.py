import os

def delete_temp_image(filename):
    try:
        os.remove(filename)
        return f'Arquivo {filename} removido com sucesso.'
    except FileNotFoundError:
        return f'O arquivo {filename} não existe.'
    except Exception as e:
        return f'Ocorreu um erro ao excluir o arquivo {filename}: {str(e)}'
