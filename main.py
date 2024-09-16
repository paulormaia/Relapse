from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from models import Usuario
from controllers.usuarios import bp_usuarios
from utils import db, lm
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine




app = Flask(__name__)

app.register_blueprint(bp_usuarios, url_prefix = '/usuario')
app.config['SECRET_KEY'] = 'senha'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
conexao = "mysql+pymysql://paulo:Relapse#17@relapse.mysql.database.azure.com/relapse"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao



db.init_app(app)
lm.init_app(app)
lm.login_view = 'usuarios.usuario_login'
migrate = Migrate(app, db)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/perfil')
@login_required
def perfil():

    if current_user.is_authenticated:

        return render_template('perfil.html')
    else:
        return redirect('/usuario/login')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000, debug = True)
