import mysql.connector

cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac",  
)

cursor = cnx.cursor()

idade1_aluno = input("Digite a menor idade a ser buscada:")
idade2_aluno = input("Digite a maior idade a ser buscada:")


query = "SELECT nome, idturma, alergias FROM aluno WHERE idade >= %s AND idade <= %s AND alergias = 'leite' is FALSE"
cursor.execute(query, (idade1_aluno, idade2_aluno,))

resultados =  cursor.fetchall()
if resultados:
    for nome, idturma, alergia in resultados:
        print(f"Nome:{nome} Turma:{idturma}")

cursor.close()
cnx.close()