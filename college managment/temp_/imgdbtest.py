import sqlite3
c=sqlite3.connect('temp_/imgdbtest.db')
cursor = c.cursor()
print("Successfully Connected to SQLite")
cursor.execute("""CREATE TABLE IF NOT EXISTS IMG(num INTEGER,img BLOB)""")
c.commit()
with open('temp_/1.png','rb') as f:
    d=f.read()
cursor.execute("INSERT INTO IMG VALUES(?,?)",(1,d))
c.commit()
cursor.execute('SELECT * FROM IMG')
a=cursor.fetchall()
t=a[0][1]
print(t)

with open('temp_/face.png','wb') as q:
    q.write(t)

cursor.close()