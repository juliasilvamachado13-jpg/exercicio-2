from flask import Flask, render_template, request, redirect, url_for, flash, abort, session
from database import conectar, criar_tabelas
from repositorios import ProdutoRepositorio
from servicos import ServicoProdutos
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "chave_secreta_padrao")

def obter_servico_produtos():
    conexao = conectar()
    criar_tabelas(conexao)
    repo = ProdutoRepositorio(conexao)
    return ServicoProdutos(repo)

@app.route("/saude")
def saude():
    return "ok"

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    servico = obter_servico_produtos()
    produtos = servico.repositorio.listar()
    return render_template("produtos.html", produtos=produtos)

@app.route("/produtos", methods=["POST"])
def cadastrar_produto():
    usuario_logado = session.get("usuario", {"perfil": "comum"}) # Simulação de sessão
    servico = obter_servico_produtos()
    try:
        servico.cadastrar(usuario_logado, request.form)
        flash("Produto cadastrado com sucesso!", "sucesso")
    except PermissionError as e:
        abort(403)
    except ValueError as e:
        flash(str(e), "erro")
    return redirect(url_for("listar_produtos"))
