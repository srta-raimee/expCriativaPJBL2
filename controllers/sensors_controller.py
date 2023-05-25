from flask import request, render_template, Blueprint, redirect, url_for
from models import *

sensors = Blueprint("sensors", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

  

@sensors.route("/registrar_sensor", methods=["POST"])
def registrar_sensor():
    nome = request.form.get('nome', None)
    descricao = request.form.get('descricao', None)
    tipo = request.form.get('tipo', None)
    limite_proximidade = request.form.get('limite_proximidade', None)
    
    Sensor.adicionar_sensor(nome, descricao, tipo, limite_proximidade)
  
    return redirect(url_for('render.listar_sensores'))
















 