from flask import Flask, request, jsonify
from db.connect_to_db import test_connection
from utils.find_testtube import find_testtube
from utils.delete_temp_img import delete_temp_image
from werkzeug.utils import secure_filename
import os
import base64
import cv2

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
    if 'file' not in request.files:
        return jsonify({'error': 'Sem arquivos enviados'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Nenhuma imagem selecionada'})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Encontrar as imagens correspondentes ao teste
        images = find_testtube(file_path)
            
        # Converter as imagens para base64
        base64_images = []
        for result, original in images:
            # Converter imagens para base64
            _, buffer = cv2.imencode('.jpg', original)
            base64_image = base64.b64encode(buffer).decode('utf-8')
            base64_images.append(base64_image)
        
        # Excluir a imagem temporária
        delete_temp_image(file_path)
        
        # Preparar os dados de resposta
        response_data = {'success': 'Imagem carregada com sucesso',
                        'images': base64_images}
        
        return jsonify(response_data)

    else:
        return jsonify({'error': 'Tipos de imagem permitidos são - png, jpg, jpeg, gif'})
