from flask import Flask, request, jsonify, redirect, render_template, session
from hashlib import sha256
from conexao import Conexao
from usuario import BancoDeDados
from carrinho import Carrinho
import random

app = Flask(__name__)
app.secret_key = "anas"

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
    
@app.route("/add_carrinho", methods=["POST"])
def add_carrinho():
    if "usuario" not in session:
        return redirect("/indexface")
    
    id_produto = request.form['id_produto']
    qtd_carrinho = 1
    email_usuario = session['usuario']['email_usuario']

    mybd = Conexao.conectar()
    cursor = mybd.cursor()

    sql = "INSERT INTO tb_carrinho (qtd_carrinho, id_produto, email_usuario) VALUES (%s, %s, %s)"

    cursor.close()
    mybd.close()

    return render_template("/carrinho")

@app.route("/carrinho")
def mostrar_carrinho():
    email_usuario = session['usuario']['id_cliente']
    produtos = Carrinho.get_carrinho(email_usuario)
    return render_template("carrinho.html", produtos=produtos)

@app.route("/cadastro")
def pagina_cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    email = request.form["email"]
    senha = request.form["senha"]

    # Aqui você pode chamar o método para cadastrar o usuário no banco de dados
    banco = BancoDeDados()
    banco.cadastrar_usuario(email, senha, nome)

    # Mensagem de sucesso
    mensagem = "Cadastro realizado com sucesso"

    # Renderiza a página de cadastro com a mensagem de sucesso
    return render_template("cadastro.html", mensagem=mensagem)



    

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    senha = request.form["senha"]

    banco = BancoDeDados()
    usuario = banco.verificar_login(email, senha)

    if usuario:
        mensagem = "Login bem-sucedido!"
        return render_template("indexface.html", mensagem=mensagem)
    else:
        mensagem = "Email ou senha incorretos. Tente novamente."
        return render_template("indexface.html", mensagem=mensagem)

@app.route('/emails_cadastrados')
def emails_cadastrados():
    banco = BancoDeDados()
    emails = banco.listar_emails()
    return render_template('emails_cadastrados.html', emails=emails)


@app.route('/comentario.html')
def comentario():
    return render_template('comentario.html')

if __name__ == "__main__":
    app.run(debug=True)