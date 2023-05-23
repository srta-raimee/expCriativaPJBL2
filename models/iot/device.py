from models import *

# class Device(db.Model):
#     __tablename__ = "devices"
#     id = db.Column("id", db.Integer(), primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     brand = db.Column(db.String(30))
#     model = db.Column(db.String(30))
#     voltage = db.Column(db.Float(), nullable=False)
#     description = db.Column(db.String(512))
#     is_active = db.Column(db.Boolean(), nullable=False, default=False)

#     sensors = db.relationship("Sensor", backref="devices", lazy=True)
#     actuators = db.relationship("Actuator", backref="devices", lazy=True)

class Dispositivo(db.Model):
    __tablename__ = 'dispositivo'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(255))
    status = db.Column(db.Boolean, default=False)

    sensores = db.relationship('Sensor', backref='dispositivos', lazy=True)
    acoes = db.relationship('Acao', backref='dispositivos', lazy=True)


    # def __init__(self, nome, descricao):
    #     self.nome = nome
    #     self.descricao = descricao

def adicionar_dispositivo(nome, descricao):
    dispositivo = Dispositivo(nome=nome, descricao=descricao)
    db.session.add(dispositivo)
    db.session.commit()

def atualizar_dispositivo(dispositivo_id, nome, descricao):
    dispositivo = Dispositivo.query.get(dispositivo_id)
    if dispositivo:
        dispositivo.nome = nome
        dispositivo.descricao = descricao
        db.session.commit()
        return dispositivo
    

# Método para Exclusão de Registros - Dispositivo
def excluir_dispositivo(dispositivo_id):
    dispositivo = Dispositivo.query.get(dispositivo_id)
    if dispositivo:
        db.session.delete(dispositivo)
        db.session.commit()
        return True
    return False


# Método para Listagem de Registros - Dispositivo
def listar_dispositivos():
    dispositivos = Dispositivo.query.all()
    return dispositivos


# Método para Listagem de Registros - Sensor
def listar_sensores():
    sensores = Sensor.query.all()
    return sensores


# Método para Listagem de Registros - Ação
def listar_acoes():
    acoes = Acao.query.all()
    return acoes
