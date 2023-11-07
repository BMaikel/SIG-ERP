from bd_cnn import Database
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginMananger

app = Flask(__name__)
app.secret_key = "MySecretKey"
db = Database()

#LOGIN ------------------------------------------------------------
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        pwd = request.form["pass"]

        user = db.buscar_usuario(username, pwd)

        if user != None:
            session["username"] = user[1]
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error = "Usuario o contraseña no válido :c")
        
    else:
        return render_template("login.html")

#DASHBOARD P1 -----------------------------------------------------
@app.route('/home')
def home():
    if "username" in session:
        return "Página permitida solo con Inicio de Sesión :3"
    else:
        return "Inicia sesión perro"

if __name__ == "__main__":
    app.run(debug=True)