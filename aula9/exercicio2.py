import mysql.connector

cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac",  
)

cursor = cnx.cursor()

idade1_aluno = input("Coloque aqui sua idade:")
idade2_aluno = input("Coloque aqui sua idade:")

query = "SELECT nome, idturma FROM aluno WHERE idade >%s AND idade < %s"
cursor.execute(query, (idade1_aluno, idade2_aluno,))

resultados =  cursor.fetchall()
if resultados:
    for nome, idturma in resultados:
        print(f"Nome:{nome} Turma:{idturma}")


cursor.close()
cnx.close()