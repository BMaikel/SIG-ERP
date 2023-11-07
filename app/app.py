from bd_cnn import Database

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = "MySecretKey"

db = Database()

#LOGIN ------------------------------------------------------------
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        pwd = request.form["pass"]

        user = db.buscar_usuario(username, pwd)

        if user:

            session["id"]           = user[0]
            session["nombres"]      = user[1]
            session["apellidos"]    = user[2]
            session['usuario']      = user[4]
            session["pass"]         = user[5]

            return redirect(url_for('index'))
        
        else:
            return render_template("login.html", error = "Usuario o contraseña no válido :c")  
    else:
        return render_template("login.html")
    

@app.route('/logout')
def logout():
    session.pop('id', None)
    session.pop('nombres', None)
    session.pop('apellidos', None)
    session.pop('usuario', None)
    session.pop('pass', None)
    return redirect(url_for('index'))

#DASHBOARD P1 -----------------------------------------------------
@app.route('/')
def index():
    if 'usuario' in session:
        return render_template("home_c.html")
    
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)