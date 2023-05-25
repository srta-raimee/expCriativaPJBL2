from models import *

class Dispositivo(db.Model):
    __tablename__ = 'dispositivo'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(255))
    status = db.Column(db.Boolean, default=False)

    sensores = db.relationship('Sensor', backref='dispositivo', lazy=True)
    acoes = db.relationship('Acao', backref='dispositivo', lazy=True)


 
    def adicionar_dispositivo(nome, descricao, status): #, dispositivo_id
   
            dispositivo = Dispositivo(nome=nome, descricao=descricao, status=status) # , dispositivo_id=dispositivo_id
            db.session.add(dispositivo)
            db.session.commit()
            # return dispositivo

    def ver_dispositivos():
        dispositivos = Dispositivo.query.all()
      
        return dispositivos
    
    def delete_dispositivo(id):
        try:
            Dispositivo.query.filter_by(id=id).delete()
            Sensor.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False
      
    def update_dispositivo(data):
        Dispositivo.query.filter_by(id=data['id'])\
                .update(dict(nome = data['nome'], descricao=data['descricao'], tipo=data['tipo'], status=data['status']))
        
        db.session.commit()
