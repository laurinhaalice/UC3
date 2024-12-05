import mysql.connector

# Conexão com o banco de dados
cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac",  
    ssl_disabled=True     
)

cursor = cnx.cursor()

query = "SELECT nome, idade, tipo_sanguineo FROM aluno;"

cursor.execute(query)


resultados = cursor.fetchall()

for nome, idade, tipo_sanguineo in resultados:
    if tipo_sanguineo == "B+" or "B-" or "O-" or "O+":
        print(f"Possível doador:{nome}, {idade}")

cursor.close()
cnx.close()