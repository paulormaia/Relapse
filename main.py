from operator import truediv
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from models import Usuario
from controllers.usuarios import bp_usuarios
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.register_blueprint(bp_usuarios, url_prefix = '/usuario')

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug = True)
