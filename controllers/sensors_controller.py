from flask import request, render_template, Blueprint, redirect, url_for
from models import *

sensors = Blueprint("sensors", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@sensors.route("/listar_sensores", methods = ["get"])
def listar_sensores():
    sensores = Sensor.query.all()
    return render_template("list.html", sensores=sensores)
    # sensores = Sensor.query.all()
    # return sensores
    # return fk.render_template("list.html", sensores=sensores, tempos=tempos, qtd=qtd, tempoTrav=tempoTrav ) # declarando todas as listas que podem ser usadas posteriormente


@sensors.route("/registrar_sensor", methods=["POST"])
def registrar_sensor():
    print("minhabunda"*100)
    nome = request.form.get('nome', None)
    descricao = request.form.get('descricao', None)
    tipo = request.form.get('tipo', None)
    limite_proximidade = request.form.get('limite_proximidade', None)

    # Faça o que for necessário com os dados do formulário
    # Por exemplo, chame a função Sensor.adicionar_sensor() aqui
    
    Sensor.adicionar_sensor(nome, descricao, tipo, limite_proximidade)
    print("minhabunda"*100)
    # return redirect(url_for('render.listar_sensores'))

# @sensors.route("/registrar_sensor", methods=["post"]) # vai ser chamado pelo botão no form html usando a chamaada action
# def regis_sens():
#     nome = fk.request.form.get('nome',None)
#     descricao = fk.request.form.get('descricao', None)
#     tipo = fk.request.form.get('tipo', None)
#     limite_proximidade = fk.request.form.get('limite_proximidade', None)


#     Sensor.adicionar_sensor(nome, descricao, tipo, limite_proximidade)
#     return fk.redirect(fk.url_for('listar_sensores'))