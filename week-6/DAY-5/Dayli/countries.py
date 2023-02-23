import psycopg2
import requests
import random 

link = "https://restcountries.com/v3.1/all"
# jai copier le lien opi pour avoir toute les data sur mon ordi 

data = requests.get(link).json()
# requests c toute les data que jai dans le link et je le transfere dans json

# capital = data[0]['capital'][0]
# le dernier 0 cest pour me donner la valeur et non me le mettre en list

# subregion = data[0]['subregion']
# print(type(subregion))

# population = data[0]['population']
# print(type(population))

# flag = data[0]['flag']
# print(flag)


USERNAME = 'postgres'
PASSWORD = '12345'
DATABASE = 'countries'
HOSTNAME = 'localhost'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor() # the cursor is the tool to run queries
query = 'select * from countries'
cursor.execute(query)
results = cursor.fetchall()
# fetchall = prend tout ce que jai ecris avant et me limprime(print sur sql)
print(results)


for i in range(10):
    rnd = random.randint(0, 25)
    name = data[rnd]['name']['common']
    capital = data[rnd]['capital'][0]
    flag = data[rnd]['flag']
    subregion = data[rnd]['subregion']
    population = data[rnd]['population']
    print(name, capital, subregion, flag, population)
    cursor.execute(f"insert into countries (name,capital,subregion,flag,population) values ('{name}','{capital}','{subregion}', '{flag}', '{population}')")

connection.commit()

connection.close()

