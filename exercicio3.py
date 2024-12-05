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

query = "SELECT nome, sexo, naturalidade FROM aluno WHERE (sexo = 'M' and naturalidade = 'Rio de Janeiro') or (sexo = 'F' and naturalidade = 'São Paulo');"

cursor.execute(query)

resultados = cursor.fetchall()

for nome, sexo, naturalidade in resultados:
   print(nome, sexo, naturalidade)

cursor.close()
cnx.close()
