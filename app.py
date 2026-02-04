from flask import Flask, render_template, request, redirect, url_for, flash
from utils import db
import os
from flask_migrate import Migrate
from models import Usuario

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_usuario = os.getenv('DB_USERNAME')
db_senha = os.getenv('DB_PASSWORD')
db_mydb = os.getenv('DB_DATABASE')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

conexao = f"mysql+pymysql://{db_usuario}:{db_senha}@{db_host}:{db_port}/{db_mydb}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        if usuario == "admin" and senha == "123":
            return "Login realizado com sucesso!"

    return render_template("login.html")

@app.route("/recuperar-senha")
def recuperar_senha():
    return render_template("recuperarsenha.html")

@app.route("/projetos")
def projetos():
    lista_projetos = [
        {"nome": "PISEW - Integrando Crianças Warao"},
        {"nome": "IFTech - Feira de Tecnologia"},
        {"nome": "Robótica ZN"},
        {"nome": "ASTRA - Ambiente de Saberes e Transmissão de Resultados Acadêmicoos"}
    ]
    return render_template("projetos.html", projetos=lista_projetos)

@app.route('/projeto/<nome>')
def projeto(nome):
    return render_template('projeto_detalhe.html', nome=nome)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        usuario = request.form.get('usuario')
        nascimento = request.form['nascimento']
        email = request.form['email']
        telefone = request.form['telefone']
        senha = request.form['senha']
        return redirect(url_for('sucesso'))
    return render_template('cadastro.html')

@app.route('/sucesso')
def sucesso():
    return "<h2>Cadastro realizado com sucesso!</h2>"

@app.route('/editarperfil')
def editar():
    return render_template("editarperfil.html")

@app.route('/editarorientador')
def editarorientador():
    return render_template("editarorientador.html")

@app.route('/areaaluno')
def areaaluno():
    return render_template("areaaluno.html")

@app.route('/areaservidor')
def areaservidor():
    return render_template("areaservidor.html")

@app.route('/editarprojeto')
def editarprojeto():
    return render_template("editarprojeto.html")

@app.route('/criarprojeto')
def criarprojeto():
    return render_template("criarprojeto.html")

@app.route('/detalhesprojeto')
def detalhesprojeto():
    return render_template("detalhesprojeto.html")

@app.route('/visualizarprojetos')
def visualizarprojetos():
    return render_template("visualizarprojetos.html")    


db.init_app(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True, port=5001)

