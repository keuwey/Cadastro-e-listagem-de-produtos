from flask import Flask, render_template, request, redirect, url_for
from models.models import db, Produto

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///produtos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Usar um contexto de aplicativo para criar as tabelas
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    produtos = Produto.query.order_by(Produto.valor).all()
    return render_template("index.html", produtos=produtos)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        valor = float(request.form["valor"])
        disponivel = request.form["disponivel"] == "sim"

        novo_produto = Produto(nome=nome, descricao=descricao, valor=valor, disponivel=disponivel)
        db.session.add(novo_produto)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("cadastro.html")


@app.route("/produto/<int:produto_id>")
def detalhes_produto(produto_id: int):
    produto = Produto.query.get_or_404(produto_id)
    return render_template("detalhes.html", produto=produto)


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
