import mysql.connector

class BancoDeDados:
    def __init__(self):
        try:
            self.conexao = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="root",
                database="theface"
            )
            if self.conexao.is_connected():
                print("Conexão com o banco de dados estabelecida com sucesso!")
            else:
                print("Falha ao conectar ao banco de dados.")
            self.cursor = self.conexao.cursor()
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")

    def __del__(self):
        self.conexao.close()

    def cadastrar_usuario(self, email, senha, nome):
        try:
            self.cursor.execute('INSERT INTO tb_usuario (email, senha, nome) VALUES (%s, %s, %s)', (email, senha, nome))
            self.conexao.commit()
            print("Cadastro realizado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao cadastrar usuário: {err}")

    def verificar_login(self, email, senha):
        try:
            self.cursor.execute('SELECT * FROM tb_usuario WHERE email = %s AND senha = %s', (email, senha))
            usuario = self.cursor.fetchone()
            return usuario
        except mysql.connector.Error as err:
            print(f"Erro ao verificar login: {err}")
        
    def listar_usuarios(self):
        try:
            self.cursor.execute('SELECT * FROM tb_usuario')
            usuarios = self.cursor.fetchall()
            for usuario in usuarios:
                print(usuario)  # Ou faça o que quiser com os dados do usuário
        except mysql.connector.Error as err:
            print(f"Erro ao listar usuários: {err}")

def fazer_login():
    banco = BancoDeDados()
    email = input("Digite o seu email: ")
    senha = input("Digite a sua senha: ")
    usuario = banco.verificar_login(email, senha)
    if usuario:
        print("Login bem-sucedido!")
    else:
        print("Email ou senha incorretos. Tente novamente.")           

def fazer_cadastro():
    banco = BancoDeDados()
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")
    senha = input("Digite a sua senha: ")
    banco.cadastrar_usuario(email, senha, nome)



if __name__ == "__main__":
    fazer_cadastro()
    fazer_login()
    banco = BancoDeDados()
    banco.listar_usuarios()