import mysql.connector

cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac",  
)


cursor = cnx.cursor()

print("Faça aqui seu cadastro.")
cadastro = input("Coloque aqui seu usuário:")
senha = input("Coloque aqui sua senha:")

query = "INSERT INTO usuario_secretaria (usuario, senha) VALUES (%s, %s)"
cursor.execute(query, (cadastro, senha,))
cnx.commit()
usuario2 = ("Coloque aqui seu usuário:")
query1 = ("SELECT usuario, senha FROM usuario_secretaria where usuario = usuario2 ")
cursor.execute(query1,)

resultados =  cursor.fetchone()
if resultados:
    for usuario, senha in resultados:
        print("Sucesso.")
else:
    print("Falha.")

cursor.close()
cnx.close()


