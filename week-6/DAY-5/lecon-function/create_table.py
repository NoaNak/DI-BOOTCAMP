import psycopg2
from datetime import date

USERNAME = 'postgres'
PASSWORD = '12345'
DATABASE = 'hollywood'
HOSTNAME = 'localhost'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

cursor = connection.cursor() # the cursor is the tool to run queries

def run_query(query: str) -> list:

    cursor.execute(query)

    try:
        output = cursor.fetchall() # the cursor also holds the output from the query
    except:
        connection.commit()

    return output


query1 = "select * FROM actors;"
query2 = "select * from actors where last_name = 'Krasinsky';"

print(run_query(query1))


title = "Titanic"
release_date = date(2002, 10, 12)
actor = 5

query3 = f"INSERT INTO movies (title, release_date, actor) values ('{title}', '{release_date}', {actor});"

run_query(query3)