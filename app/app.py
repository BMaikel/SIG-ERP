from bd_cnn import Database
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "MySecretKey"
db = Database()

#LOGIN ------------------------------------------------------------
@app.route("/login", methods = ["GET", "POST"])
def login():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True) 