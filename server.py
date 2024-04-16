from flask import Flask
from db.connect_to_db import test_connection

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/db')
def validate_db_conn():
    if test_connection():
        return 'Conexão realizada com sucesso'
    else:
        return 'Falha ao conectar ao banco de dados.'

@app.route('/db/create_image', methods=['POST'])
def validate_img_creation():
    if validate_db_conn():
        return 'Função de criação de imagem'

if __name__ == '__main__':
    app.run(debug=True)
