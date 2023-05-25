from flask import request, render_template, Blueprint, redirect, url_for
from models import *

dispositivos = Blueprint("dispositivos", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

  

@dispositivos.route("/registrar_dispositivo", methods=["POST"])
def registrar_dispositivo():
    nome = request.form.get('nome_disp', None)
    descricao = request.form.get('descricao_disp', None)
    status = request.form.get('status', None)
    
    # Verificar o valor do status
    if status == 'True':
        status_bool = True
    else:
        status_bool = False

    Dispositivo.adicionar_dispositivo(nome, descricao, status_bool)
  
    return redirect(url_for('render.listar_dispositivos'))