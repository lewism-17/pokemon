import sqlite3 as sql
#import makeDatabase

db = sql.connect("pokemon.db")
c = db.cursor()

c.execute("SELECT * FROM Pokemon")
results = c.fetchall()

for line in results:
   print(line)
    
print("All Done")
