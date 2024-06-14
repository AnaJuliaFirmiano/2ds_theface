from flask import Flask, request, jsonify, redirect, render_template, session
from hashlib import sha256
from conexao import Conexao

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    produtos = []

    mybd = Conexao.conectar()
    cursor = mybd.cursor()

    cursor.execute("SELECT id_do_produto, nome, valor, descricao, foto FROM tb_produto ")
    produtos = cursor.fetchall()

    cursor.close()
    mybd.close()

    return render_template('indexface.html', produtos=produtos)
    
@app.route("/carrinho")
def ver_carrinho():
    carrinho_detalhes = []

    if "carrinho" not in session:
        session["carrinho"] = {}

    mybd = Conexao.conectar()
    cursor = mybd.cursor()

    for produto_id, quantidade in session["carrinho"].items():
        cursor.execute("SELECT nome, valor FROM tb_produto WHERE id_do_produto = %s", (produto_id))
        produto = cursor.fetchone()
        carrinho_detalhes.append({"nome": produto[0], "valor": produto[1], "quantidade": quantidade})


    cursor.close()
    mybd.close()

    return render_template("carrinho.html", carrinho_detalhes=carrinho_detalhes)


if __name__ == "__main__":
    app.run(debug=True)