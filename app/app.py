import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename


app = Flask(__name__)

# no arquivo config.py, contém variáveis do FLASK que permite
# definir valores diferentes do padrão, ou acrescentar novas variáveis
# para ser usado no projeto, como UPLOAD_FOLDER
app.config.from_object("config")


# o Blueprint permite criar e registrar rotas/endpoints de outros pacotes 
# do projeto. Então, se temos um projeto como "API", criamos as rotas nesse projeto
# e nesse arquivo, usamos a função register_blueprint para registrar as rotas da API
from .routes import main
from .api.routes import api
app.register_blueprint(main)
app.register_blueprint(api)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



def allowed_file(filename):
    allowed_extensions = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


@app.route("/secure")
def route_with_protection():
    print("Usuário não autorizado")
    # redirecionamos o usuário ao endpoint do @app para a função hello_world()
    # poderiamos fazer também redirect("/")
    return redirect(url_for(".hello_world"))


@app.route('/upload', methods=['POST'])
def upload_file():
    # validamos se existe a variavel "file" na requisição
    if 'file' not in request.files:
        flash('arquivo não enviado')
        return "arquivo não enviado", 400
    
    file = request.files['file']
    
    # Se o usuário faz uma requisição mas o arquivo If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('Arquivo está vazio')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        return f"file {filename} upload with success", 200
    
    return "Invalid file", 400