from models import *

class Sensor(db.Model):
    __tablename__ = 'sensor'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(255))
    tipo = db.Column(db.String(50))
    limite_proximidade = db.Column(db.Float)

    dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id'))
    # dispositivo = db.relationship('Dispositivo', backref=db.backref('sensores', lazy='dynamic'))
    registros = db.relationship('Read', backref='sensor', lazy=True)

    # def __init__(self, nome, descricao, tipo, limite_proximidade, dispositivo):
    #     self.nome = nome
    #     self.descricao = descricao
    #     self.tipo = tipo
    #     self.limite_proximidade = limite_proximidade
    #     self.dispositivo = dispositivo

    def adicionar_sensor(nome, descricao, tipo, limite_proximidade): #, dispositivo_id
  
            sensor = Sensor(nome=nome, descricao=descricao, tipo=tipo, limite_proximidade=limite_proximidade) # , dispositivo_id=dispositivo_id
            db.session.add(sensor)
            db.session.commit()
            # return sensor

    def ver_sensores():
        sensors = Sensor.query.all()
      
        return sensors
    
    def delete_sensor(id):
        try:
            Sensor.query.filter_by(id=id).delete()
            Dispositivo.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False
      
    def update_sensor(data):
        Sensor.query.filter_by(id=data['id'])\
                .update(dict(nome = data['nome'], descricao=data['descricao'], tipo=data['tipo'], limite_proximidade=data['limite_proximidade']))
     
        db.session.commit()
   