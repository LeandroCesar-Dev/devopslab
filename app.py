from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app) 

@app.route("/")
def pagina_inicial():
    return "<h1>Hello DevOps - Muito Show esse lab Parabéns Gaby</h1><br><hr>Laboratório Pipeline DevOps"

if __name__ == '__main__':
    app.run()