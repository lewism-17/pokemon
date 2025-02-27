import sqlite3 as sql


db = sql.connect("pokemon.db")
c = db.cursor()

c.execute("DROP TABLE IF EXISTS Pokemon")
c.execute("CREATE TABLE Pokemon (ID INTEGER, name TEXT, type1 TEXT, type2 TEXT, hp INTEGER, attack INTEGER, defence INTEGER, speed INTEGER)")

f = open("pokemon.csv","r")
for line in f:
    bits = line.split(",")
    c.execute("INSERT INTO Pokemon VALUES (?,?,?,?,?,?,?,?)", bits)    
db.commit()

print("Made Database")