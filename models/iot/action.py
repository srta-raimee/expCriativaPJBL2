from models import *

class Acao(db.Model):
    __tablename__ = 'acao'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(255))
    tipo = db.Column(db.String(50))

    dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id'))
    dispositivo = db.relationship('Dispositivo', backref=db.backref('acoes', lazy='dynamic'))

    def __init__(self, nome, descricao, tipo, dispositivo):
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo
        self.dispositivo = dispositivo