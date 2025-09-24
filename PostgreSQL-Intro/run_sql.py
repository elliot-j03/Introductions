import psycopg2

connection = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="postgres",
    user="postgres",
    password="password"
)

cursor = connection.cursor()

with open("schema.sql", "r") as file:
    sql_query = file.read()

cursor.execute(sql_query)


connection.commit()
cursor.close()
connection.close()