# PHrecognition
App based in Python for PH recognition through pictures 

Vai precisar de Flask, OpenCV e o driver psycopg2 pra poder 
trabalhar com banco de dados.


# Pra instalar o Flask:

pip install flask

# Para o OpenCV:

pip install opencv-python

# Isso instalará a versão mais recente da biblioteca OpenCV em seu ambiente Python.
# Se você deseja instalar uma versão específica do OpenCV, você pode especificar a versão
# desejada no comando pip. Por exemplo:

pip install opencv-python==4.5.4.58

# Pra instalar o driver:

pip install psycopg2

# Explicação da estrutura de pastas:

api/: Esta pasta contém o código relacionado à API, incluindo os endpoints, modelos (ou schemas) de dados e utilitários.

endpoints/: Aqui ficam os arquivos que definem os endpoints da API. Cada arquivo pode conter a lógica para um conjunto de endpoints relacionados.

models/: Aqui ficam os arquivos que definem os modelos de dados usados pela API. Eles geralmente consistem em classes Python que representam os dados da aplicação.

utils/: Esta pasta contém utilitários ou funções auxiliares que são compartilhados por vários componentes da API.

tests/: Esta pasta contém os arquivos de teste para os diferentes componentes da API.

config/: Esta pasta contém arquivos de configuração para a aplicação, como configurações de ambiente, variáveis de ambiente, etc.

scripts/: Aqui ficam os scripts Python auxiliares que podem ser úteis para tarefas de administração, tarefas de manutenção, etc.

requirements.txt: Um arquivo que lista as dependências Python necessárias para executar a aplicação. Isso pode ser gerado usando o comando pip freeze > requirements.txt após a instalação de todas as dependências necessárias.

README.md: Um arquivo markdown que contém informações sobre o projeto, incluindo uma descrição, instruções de instalação, exemplos de uso, etc.

Essa estrutura de pastas é apenas uma sugestão e pode ser adaptada conforme necessário para atender às especificidades do seu projeto. O objetivo principal é manter o código organizado, modular e de fácil manutenção.
