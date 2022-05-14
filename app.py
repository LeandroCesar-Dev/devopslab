from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello DevOps - Muito Show esse lab - Parabéns Gaby"

if __name__ == '__main__':
    app.run()