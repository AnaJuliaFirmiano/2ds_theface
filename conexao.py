import mysql.connector

class Conexao():
    @staticmethod
    def conectar():
        mybd = mysql.connector.connect(
            host = "127.0.0.1",
            port = 3306,
            user = "root",
            password = "root",
            database = "theface"
        )
    
        return mybd

# Criar conexão banco de dados
mybd = Conexao.conectar()

try:
    mycursor = mybd.cursor()

finally:
    mycursor.close()
    mybd.close()