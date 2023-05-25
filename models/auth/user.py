from models import db, Role
from bcrypt import hashpw, gensalt
from sqlalchemy import or_
from flask_login import UserMixin



class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column("id",  db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(1024), nullable=False) 
    cpf = db.Column(db.String(30), nullable=False) 
    id_role = db.Column(db.Integer(), db.ForeignKey(Role.id))
    
    roles = db.relationship("Role", back_populates="users", secondary="user_roles")
    reads = db.relationship("Read", backref="users", lazy=True)    
    
    def get_users():
        users = User.query.all()
        
        return users
    
    def set_password(self, password):
        self.password = hashpw(password.encode(), gensalt()).decode()
        # password = password

    def check_password(self, password):
        return hashpw(password.encode(), self.password.encode()) == self.password.encode()

    def save_user(username, email, password, cpf, id_role):
        user = User(username=username, email=email, cpf=cpf, id_role=id_role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

    def check_login(login_info):
        if "@" in login_info:
            user = User.query.filter_by(email=login_info).first()
        else:
            user = User.query.filter_by(username=login_info).first()
        return user

    @classmethod
    def check_login2(cls, username, email):
        user = cls.query.filter(or_(cls.username == username, cls.email == email)).first()
        return user
                