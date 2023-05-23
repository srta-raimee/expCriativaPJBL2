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
        # from models import Dispositivo
        # dispositivo = Dispositivo.query.get(dispositivo_id)
        # if dispositivo:
            sensor = Sensor(nome=nome, descricao=descricao, tipo=tipo, limite_proximidade=limite_proximidade) # , dispositivo_id=dispositivo_id
            db.session.add(sensor)
            db.session.commit()
            # return sensor

    def ver_sensores():
        sensors = Sensor.query.all()
        #   sensors = Sensor.query.join(Device, Device.id == Sensor.id)\
        #             .add_columns(Sensor.id, Device.name, Device.brand, Device.model, 
        #                          Device.voltage, Device.description,  Device.is_active, Sensor.measure).all()
        
        return sensors
    
    def delete_sensor(id):
        try:
            Sensor.query.filter_by(id=id).delete()
            Dispositivo.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False
    # def excluir_sensor(sensor_id):
    #     sensor = Sensor.query.get(sensor_id)
    #     if sensor:
    #         db.session.delete(sensor)
    #         db.session.commit()
    #         return True
    #     return False

    def atualizar_sensor(sensor_id, nome, descricao, tipo, limite_proximidade):
        sensor = Sensor.query.get(sensor_id)
        if sensor:
            sensor.nome = nome
            sensor.descricao = descricao
            sensor.tipo = tipo
            sensor.limite_proximidade = limite_proximidade
            db.session.commit()
            return sensor


    # class Sensor(db.Model):
    #     __tablename__ = "sensors"
    #     id = db.Column("id", db.Integer, db.ForeignKey(Device.id), primary_key = True)
    #     measure = db.Column(db.String(20))

    #     reads = db.relationship("Read", backref="sensors", lazy=True)

    #     # def get_sensors():
    #     #     sensors = Sensor.query.join(Device, Device.id == Sensor.id)\
    #     #                 .add_columns(Sensor.id, Device.name, Device.brand, Device.model, 
    #     #                              Device.voltage, Device.description,  Device.is_active, Sensor.measure).all()
            
    #     #     return sensors
        
    #     def save_sensor(name, brand, model, description, voltage, is_active, measure):
    #         device = Device(name = name, brand = brand, model = model, 
    #                             description = description, voltage = voltage, is_active = is_active)
        
    #         sensor = Sensor(id = device.id, measure = measure)
            
    #         device.sensors.append(sensor)
    #         db.session.add(device)
    #         db.session.commit()

    #     # def delete_sensor(id):
    #     #     sensor = Sensor.query.filter(Sensor.id == id).first()
    #     #     Sensor.query.filter_by(measure="%").delete()
    #     #     sensor.delete()

    #     # def delete_sensor_by_measure(measure):
    #     #     Sensor.query.filter_by(measure=measure).delete()
    #     #     db.session.commit()

    #     # def update_sensor(data):
    #     #     Device.query.filter_by(id=data['id'])\
    #     #             .update(dict(name = data['name'], brand=data['brand'], model = data['model'], 
    #     #                     voltage = data['voltage'], description = data['description'], 
    #     #                     is_active = data['is_active']))
            
    #     #     Sensor.query.filter_by(id=data['id'])\
    #     #                     .update(dict(measure = data['measure']))
    #     #     db.session.commit()