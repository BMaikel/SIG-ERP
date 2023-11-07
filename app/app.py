from bd_cnn import Database
from user_model import User

from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, login_required, login_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "MySecretKey"

login_manager = LoginManager(app)
login_manager.login_view = 'login'

db = Database()

#LOGIN ------------------------------------------------------------
@login_manager.user_loader
def load_user(user_id):
    return db.get_user(user_id) 

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        pwd = request.form["pass"]

        resp = db.buscar_usuario(username, pwd)

        if resp != None:
            user = User(resp[0],resp[1],resp[2],resp[1])
            login_user(user)
            return redirect(url_for("home"))
        
        else:
            return render_template("login.html", error = "Usuario o contraseña no válido :c")
        
    else:
        return render_template("login.html")
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

#DASHBOARD P1 -----------------------------------------------------
@app.route('/home')
@login_required
def home():
    if "username" in session:
        return "Página permitida solo con Inicio de Sesión :3"
    else:
        return "Inicia sesión perro"

if __name__ == "__main__":
    app.run(debug=True)