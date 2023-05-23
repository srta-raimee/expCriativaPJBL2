from flask import request, render_template, Blueprint, redirect, url_for, flash
from models import *
# aqui tudo é renderizado
render = Blueprint("render", __name__, template_folder="./views/", static_folder='./static/', root_path="./")


@render.route("/")
def default_index():
    return render_template("home.html")

@render.route("/home")
def ret_home():
     return render_template("home.html")
  
@render.route("/pag_cadastro_sensor")
def pag_cad_sens():
    return render_template("sensors/cadastro_sensor.html")

@render.route("/pag_cadastro_user")
def pag_cad_user():
    return render_template("user/cadastro_user.html")

@render.route("/pag_login")
def pag_log():
    return render_template("auth/login.html") 

# @render.route("/login")
# def login():
#     global nomes, emails, senhas, cpfs
#     if nomes[i] == 

# @render.route("/listar_sensores_pag")
# def listar_sensores_pag():
#     return fk.render_template("sensors/list_sensors.html")

@render.route("/listar_users")
def listar_users():
    return render_template("user/list_users.html")

@render.route("/listar_sensores", methods = ["get"])
def listar_sensores():
    sensores = Sensor.ver_sensores()
    return render_template("sensors/list_sensors.html", sensores=sensores)

@render.route("/delete_sensor/<id>")
def delete_sensor(id):
    if Sensor.delete_sensor(id):
        flash("Dispositivo Sensor Excluído com sucesso!!", "success")
    else:
        flash("Dispositivo Sensor não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for('render.listar_sensores'))


@render.route("/about")
def about():
    return render_template("about.html")

@render.route("/project")
def projetar():
    return render_template("project.html")


# rotas post

# @render.route("/registrar_user", methods=["get", "post"]) # vai ser chamado pelo botão no form html usando a chamaada action
# def reg_user():
#     nome = fk.request.form.get('nome',None)
#     email = fk.request.form.get('email', None)
#     senha = fk.request.form.get('senha', None)
#     cpf = fk.request.form.get('cpf', None)

#     global nomes, emails, senhas, cpfs
#     nomes.append(nome)
#     emails.append(email)
#     senhas.append((senha))
#     cpfs.append(cpf)
#     print(nomes)
    
#     return fk.redirect(fk.url_for('render.pag_log')) 