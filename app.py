from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("paginas/index.html", \
        titulo_pagina="Página inicial")
    
@app.route("/times")
def categorias():
    return render_template("paginas/times.html", \
        titulo_pagina="Times")

@app.route("/jogadores")
def produto():
    return render_template("paginas/jogadores.html", \
        titulo_pagina="Jogadores")
    
@app.route("/resultado")
def carrinho():
    return render_template("paginas/resultado.html", \
        titulo_pagina="Resultados")

if __name__ == "__main__":
    app.run(debug=True)
