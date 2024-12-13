import mysql.connector

cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac",  
)


cursor = cnx.cursor()

idade_aluno = input("Digite a idade do aluno que deseja buscar:")

# Consulta paramerizada
query =  "SELECT idade, cpf, endereco FROM aluno WHERE idade = %s;"
cursor.execute(query, (idade_aluno,))

resultados =  cursor.fetchall()
if resultados:
    for cpf, endereco in resultados:
        print(f" CPF: {cpf}, Enderço: {endereco}")
else:
    print("Nenhum aluno encontrado com essa idade.")

cursor.close()
cnx.close()