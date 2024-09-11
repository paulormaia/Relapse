from utils import db, lm
from flask_login import  UserMixin

class Usuario(UserMixin, db.Model):
  __tablename__= "usuario"
  id = db.Column(db.Integer, primary_key = True)
  nome = db.Column(db.String(80), nullable=True)
  email = db.Column(db.String(100), nullable=True)
  senha = db.Column(db.String(100), nullable=True)

  def __init__(self, nome, email, senha):

    self.nome = nome
    self.email = email
    self.senha = senha

  def __repr__(self):
    return 'olá, {}!'.format(self.nome)
