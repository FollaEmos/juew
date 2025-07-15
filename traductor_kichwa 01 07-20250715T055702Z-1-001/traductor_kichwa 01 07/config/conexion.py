import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Buscar1+",
        database="traductorv2",
        charset="utf8mb4",
        use_unicode=True
    )
