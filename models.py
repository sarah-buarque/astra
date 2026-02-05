from datetime import datetime
from utils import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model, UserMixin):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    perfil = db.Column(db.String(22), nullable=False)
    nome = db.Column(db.String(150), nullable=False)
    matricula = db.Column(db.String(50), nullable=False)
    nascimento = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    telefone = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(240), nullable=False)

    def set_senha(self, senha):
        self.senha = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha, senha)

    def __repr__(self):
        return f"<Usuario {self.nome} - {self.email}>"



class Projeto(db.Model):
    __tablename__ = "projeto"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    edital = db.Column(db.String(100), nullable=True)
    nome_projeto = db.Column(db.String(150), nullable=False)
    imagem = db.Column(db.String(150), nullable=True)  
    coordenador = db.Column(db.String(100), nullable=False)
    campus = db.Column(db.String(100), nullable=False)
    vagas = db.Column(db.Integer, nullable=True)
    descricao = db.Column(db.Text, nullable=False)
    data_projeto = db.Column(db.Date, nullable=False)
    tipo_projeto = db.Column(db.String(50), nullable=False)  
   

    def __repr__(self):
        return f'<Projeto {self.nome_projeto}>'