from conexao import Conexao


class Carrinho:
    def add_carrinho(email_usuario, id_produto):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO tb_carrinho (email_usuario, id_produto) VALUES (%s, %s, %s)"
        valores = (email_usuario, id_produto)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

    def get_carrinho(email_usuario):
        conexao = Conexao.conectar()
        cursor = conexao.cursor(dictionary=True)

        sql = """
        SELECT p.nome, p.valor FROM tb_produto p INNER JOIN tb_carrinho c ON p.id_produto WHERE c.id_cliente = %s
        """

        valores = (email_usuario,)
        cursor.execute(sql, valores)
        produtos = cursor.fetchall()

        cursor.close()
        conexao.close()

        return produtos