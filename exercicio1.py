import mysql.connector

cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac",  
)

# Criação do cursor
cursor = cnx.cursor()

# Consulta
query = "SELECT nome, endereco FROM aluno;"

cursor.execute(query)

# Processar os resultados
resultados = cursor.fetchall()

for nome, endereco in resultados:
    print(nome, endereco)

# Fechando o cursor e a conexão
cursor.close()
cnx.close()