from flask import Flask, request
from db.connect_to_db import test_connection
from utils.receive_image import save_img_to_db
from utils.delete_temp_img import delete_temp_image
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = 'temp_images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# Define o tamanho máximo de arquivo permitido (em bytes)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
def upload_image():
    conn = test_connection()
    if not conn:
        return 'Falha ao conectar ao banco de dados', 500
    if 'file' not in request.files:
        return 'Sem arquivos enviados'
    file = request.files['file']
    if file.filename == '':
        return 'Nenhuma imagem selecionada'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        result = save_img_to_db(file, conn)
        if 'sucesso' in result.lower():
            delete_temp_image(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return result
    else:
        return 'Allowed image types are - png, jpg, jpeg, gif'

