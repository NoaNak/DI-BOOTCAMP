import psycopg2
import requests
import random 
import pandas as pd
import matplotlib.pyplot as plt


link = "https://restcountries.com/v3.1/all"
# jai copier le lien opi pour avoir toute les data sur mon ordi 

data = requests.get(link).json()
# requests c toute les data que jai dans le link et je le transfere dans json

USERNAME = 'postgres'
PASSWORD = '12345'
DATABASE = 'Hackathon2'
HOSTNAME = 'localhost'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor() # the cursor is the tool to run queries
query =  'select * from population'
cursor.execute(query)
# results = cursor.fetchall()
# fetchall = prend tout ce que jai ecris avant et me limprime(print sur sql)
# print(results)


# for i in range(10):
#     rnd = random.randint(0, 193)
#     name = data[rnd]['name']['common']
#     population = data[rnd]['population']
#     # print(name, population)
#     cursor.execute(f"insert into population (name, rate) values ('{name}','{population}')")

query2 = "select rate from population where name = 'Russia'"
query3 = "select rate from population where name = 'Greece'"
cursor.execute(query2)
cursor.execute(query3)
results = cursor.fetchall()
print(results)

connection.commit()
connection.close()


data = {'Russia':144104080, 'Greece':10715549}
courses = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize = (10, 5))
plt.bar(courses, values, color ='maroon',
        width = 0.4)

plt.xlabel("Countries")
plt.ylabel("Population")
plt.title("Difference of population in greece and in russia")
plt.show()

print(data)

 



