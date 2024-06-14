from flask import Flask, request, jsonify, redirect, render_template, session
from hashlib import sha256
from conexao import Conexao

app = Flask(__name__)

@app.route("/adicionar_carrinho", methods=["POST"])
def adicionar_carrinho():
    produto_id = request.form["produto_id"]
    quantidade = int(request.form["quantidade"])

    if "carrinho" not in session:
        session["carrinho"] = {}

    if produto_id in session["carrinho"]:
        session["carrinho"][produto_id] += quantidade
    else:
        session["carrinho"][produto_id] = quantidade

        return redirect("/carrinho")

@app.route("/remover_item", methods=["POST"])
def remover_item():
    produto_id = request.form["produto_id"]

    if "carrinho" in session and produto_id in session["carrinho"]:
        del session["carrinho"]["produto_id"]

    return redirect("/carrinho")

if __name__ == "__main__":
    app.run(debug=True)