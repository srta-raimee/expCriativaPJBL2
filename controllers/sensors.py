import flask as fk
from models import *
sensors = fk.Blueprint("sensors", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@sensors.route("/list_sensors", methods = ["get"])
def listar_sensores():
    sensores = Sensor.query.all()
    return render_template("list.html", sensores=sensores)
    # sensores = Sensor.query.all()
    # return sensores
    # return fk.render_template("list.html", sensores=sensores, tempos=tempos, qtd=qtd, tempoTrav=tempoTrav ) # declarando todas as listas que podem ser usadas posteriormente


@sensors.route("/registrar_sensor", methods=["get", "post"]) # vai ser chamado pelo botão no form html usando a chamaada action
def registrat_sensor():
    nome = fk.request.form.get('nome',None)
    descricao = fk.request.form.get('descricao', None)
    tipo = fk.request.form.get('tipo', None)
    limite_proximidade = fk.request.form.get('limite_proximidade', None)


    
    return fk.redirect(fk.url_for('render.listar_sensores', nome=nome, descricao=descricao, tipo=tipo, limite_proximidade=limite_proximidade)) # vai redirecionar para a função de renderização da página "listar"
