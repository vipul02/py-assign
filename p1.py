import mysql.connector

# Generator function to fetch the data with less memory in efficient manner
def fetchE(res):
    for _ in res:
        yield _

db = mysql.connector.connect(
    host='localhost', 
    user='root', 
    passwd='admin@123', 
    database='sakila'
    )

pointer = db.cursor()
pointer.execute('SELECT * FROM payment')

res = pointer.fetchall()
    
print(fetchE(res))

for _ in fetchE(res):
    print(_)
