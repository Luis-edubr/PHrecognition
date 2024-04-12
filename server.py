from flask import Flask
from db.connect_to_db import test_connection

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/db')
def get_database_file():
    if test_connection():
        return 'Conexão com o banco de dados bem-sucedida!'
    else:
        return 'Falha ao conectar ao banco de dados.'

if __name__ == '__main__':
    app.run(debug=True)
