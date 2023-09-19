q="""
    create table std_info
    (name TEXT NOT NULL,
    roll_num TEXT PRIMARY KEY,
    regis_num TEXT NOT NULL,
    dept TEXT NOT NULL,
    dob TEXT NOT NULL,
    doj TEXT NOT NULL,
    pno TEXT NOT NULL,
    address TEXT)
"""
std="""
insert into std_info values
    ('Sarvesh',195001,910619205001,'IT','01-01-2001','01-01-2019',1111111111,'north madurai'),
    ('Purnima',196002,910619205002,'IT','01-02-2002','01-01-2020',2222222222,'south madurai'),
    ('Amarjeet',196003,910619205003,'IT','01-03-2002','01-01-2020',3333333333,'south madurai'),
    ('Sumati',197004,910619205004,'IT','01-04-2003','01-01-2021',4444444444,'east madurai'),
    ('Sharma',197005,910619205005,'IT','01-05-2003','01-01-2021',5555555555,'west madurai'),
    ('Nagendra',195006,910619205006,'IT','01-06-2001','01-01-2019',6666666666,'north madurai');
"""
import sqlite3

try:
    c = sqlite3.connect('college-db.db')
    cursor = c.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(q)
    c.commit()
    cursor.execute(std)
    c.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if c:
        c.close()
        print("sqlite connection is closed")