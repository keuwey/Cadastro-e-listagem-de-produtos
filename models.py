from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Produto(db.Model):
    id: int
    nome: str
    descricao: str
    valor: float
    disponivel: bool

    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    disponivel = db.Column(db.Boolean, nullable=False)

    def __repr__(self) -> str:
        return f"<Produto {self.nome}>"
