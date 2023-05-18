import flask as fk
# aqui tudo é renderizado
render = fk.Blueprint("render", __name__, template_folder="./views/", static_folder='./static/', root_path="./")


@render.route("/")
def default_index():
    return fk.render_template("home.html")

@render.route("/home")
def ret_home():
     return fk.render_template("home.html")
  
@render.route("/pag_cadastro_sensor")
def pag_cad_sens():
    return fk.render_template("sensors/cadastro_sensor.html")

@render.route("/pag_cadastro_user")
def pag_cad_user():
    return fk.render_template("user/cadastro_user.html")

@render.route("/pag_login")
def pag_log():
    return fk.render_template("auth/login.html") 

# @render.route("/login")
# def login():
#     global nomes, emails, senhas, cpfs
#     if nomes[i] == 

@render.route("/listar_sensores")
def listar_sensores():
    return fk.render_template("sensors/sensores.html")

@render.route("/listar_users")
def listar_users():
    return fk.render_template("user/list_users.html")

@render.route("/about")
def about():
    return fk.render_template("about.html")

@render.route("/project")
def projetar():
    return fk.render_template("project.html")


# rotas post

@render.route("/registrar_user", methods=["get", "post"]) # vai ser chamado pelo botão no form html usando a chamaada action
def reg_user():
    nome = fk.request.form.get('nome',None)
    email = fk.request.form.get('email', None)
    senha = fk.request.form.get('senha', None)
    cpf = fk.request.form.get('cpf', None)

    global nomes, emails, senhas, cpfs
    nomes.append(nome)
    emails.append(email)
    senhas.append((senha))
    cpfs.append(cpf)
    print(nomes)
    
    return fk.redirect(fk.url_for('render.pag_log')) 