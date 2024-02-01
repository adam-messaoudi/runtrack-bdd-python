import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",      
    user="root",  
    password="A.m.13015",  
    database="LaPlateforme" 
)

mycursor = mydb.cursor()

sql_query = "SELECT * FROM etudiant"

mycursor.execute(sql_query)

results = mycursor.fetchall()

for row in results:
    print(row)

mycursor.close()
mydb.close()
