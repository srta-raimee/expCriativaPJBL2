import flask as fk
user = fk.Blueprint("user", __name__, template_folder="./views/", static_folder='./static/', root_path="./")


@user.route("/list_users", methods = ["get"])
def listar_users():
     global nomes, emails, senhas, cpfs
     return fk.render_template("list_users.html", nomes=nomes, emails=emails, senhas=senhas, cpfs=cpfs) 
