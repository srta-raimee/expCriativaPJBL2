import flask as fk
sensors = fk.Blueprint("sensors", __name__, template_folder="./views/", static_folder='./static/', root_path="./")


@sensors.route("/list_sensors", methods = ["get"])
def listar_sensores():
    global sensores, tempos, qtd, tempoTrav
    return fk.render_template("list.html", sensores=sensores, tempos=tempos, qtd=qtd, tempoTrav=tempoTrav ) # declarando todas as listas que podem ser usadas posteriormente


@sensors.route("/registrar_sensor", methods=["get", "post"]) # vai ser chamado pelo botão no form html usando a chamaada action
def reg_sens():
    nomeSensor = fk.request.form.get('nomeSensor',None)
    tempoLigado = fk.request.form.get('tempoLigado', None)
    qtdFaixa = fk.request.form.get('qtdFaixa', None)
    tempoTravessia = fk.request.form.get('tempoTravessia', None)

    # global sensores, tempos, qtd, tempoTrav
    # sensores.append(nomeSensor)
    # tempos.append(tempoLigado)
    # qtd.append(qtdFaixa)
    # tempoTrav.append(tempoTravessia)

    
    return fk.redirect(fk.url_for('render.listar', nomeSensor=nomeSensor, tempoLigado=tempoLigado, qtdFaixa=qtdFaixa, tempoTravessia=tempoTravessia)) # vai redirecionar para a função de renderização da página "listar"
