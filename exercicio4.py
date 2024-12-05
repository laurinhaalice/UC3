import mysql.connector

cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac",  
    ssl_disabled=True     
)

cursor = cnx.cursor()

query = "SELECT nome, cpf_responsavel1, cpf_responsavel2 FROM aluno;"

cursor.execute(query)

resultados = cursor.fetchall()

for nome, cpf_responsavel1, cpf_responsavel2 in resultados:
    print(f"{nome} tem dois responsáveis cadastrados.")

cursor.close()
cnx.close()
