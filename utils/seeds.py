# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
# from models import Dispositivo, Sensor, Acao

# def generate_seeds(db: SQLAlchemy):
#     dispositivo1 = Dispositivo(nome="Nome do Dispositivo 1", descricao="Descrição do Dispositivo 1")
#     dispositivo1.status = True  # Definir o atributo 'status' separadamente
#     db.session.add(dispositivo1)
#     db.session.commit()

#     sensor1 = Sensor(nome="Nome do Sensor 1", descricao="Descrição do Sensor 1", tipo="Tipo do Sensor 1", limite_proximidade=0.5, dispositivo=dispositivo1)
#     db.session.add(sensor1)
#     db.session.commit()

#     # Exemplo de atualização de um registro
#     sensor1.nome = "Novo Nome do Sensor 1"
#     db.session.commit()

#     acao1 = Acao(nome="Nome da Ação 1", descricao="Descrição da Ação 1", tipo="Tipo da Ação 1", dispositivo=dispositivo1)
#     db.session.add(acao1)
#     db.session.commit()

#     # Adicione aqui mais registros para as outras tabelas, se necessário


#     # Adicione aqui mais registros para as outras tabelas, se necessário


# # from datetime import datetime
# # from flask_sqlalchemy import SQLAlchemy
# # from datetime import datetime
# # from models import *


# # def generate_seeds(db:SQLAlchemy):
# #     device1 = Device(brand = "ESP32", model = "ESP32", name = "Umidade", voltage = 5, description = "Sendor de umidade com medida em percentual")
   
# #     db.session.add_all([device1]) # device2, device3, device4, device5,device6,device7,device8,device9
# #     db.session.commit()

# #     sensor1 = Sensor(id = device1.id, measure = "%")
# #     # sensor2 = Sensor(id = device2.id, measure = "ºC")
# #     # sensor3 = Sensor(id = device3.id, measure = "cm")
# #     # sensor4 = Sensor(id = device4.id, measure = "Lumens")
# #     # sensor5 = Sensor(id = device5.id, measure = "")

# #     db.session.add_all([sensor1]) # , sensor2, sensor3, sensor4, sensor5]
# #     db.session.commit()
# #     data = {}
# #     data["id"] = sensor1.id
# #     data["brand"] = device1.brand
# #     data["name"] = device1.name
# #     data["model"] = "Teste Update"
# #     data["voltage"] = device1.voltage
# #     data["description"] = device1.description
# #     data["is_active"] = False
# #     data["measure"] = "Measure Teste"
# #     Sensor.update_sensor(data)

# #     actuator1 = Actuator(id = device1.id, actuator_type = None)
# #     # actuator2 = Actuator(id = device7.id, actuator_type = "Chassi Robótico")
# #     # actuator3 = Actuator(id = device8.id, actuator_type = "ULN2003")
# #     # actuator4 = Actuator(id = device9.id, actuator_type = None)

# #     db.session.add_all([actuator1]) # , actuator2, actuator3, actuator4
# #     db.session.commit()
    
