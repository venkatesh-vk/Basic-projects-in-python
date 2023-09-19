'''
a="""
create table std_img(roll_num INTEGER PRIMARY KEY,imgs BLOB)
create table std_info (name TEXT NOT NULL,roll_num INTEGER PRIMARY KEY,regis_num INTEGER NOT NULL,dept TEXT NOT NULL,dob DATE,pno INTEGER NOT NULL,address TEXT)\n
create table Python (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table Cpp (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table C (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table java (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table m1 (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table m2 (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table m3 (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table m4 (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table m5 (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table dpsd (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table beee (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table cn (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table os (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table adc (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table comm (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table eng1 (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table eng2 (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table sysdes (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table dsalgo (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table webdev (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table ml (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table softcomp (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table micro (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table evs (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table dbms (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table daa (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table ca (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table eg (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table bigdata (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table elec1 (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ct1 INTEGER,ct2 INTEGER,ct3 INTEGER,cit1 INTEGER,cit2 INTEGER,cit3 INTEGER,ext INTEGER)\n
create table mini (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ext INTEGER)\n
create table final (roll_num INTEGER PRIMARY KEY,staff_id INTEGER NOT NULL,dept TEXT,ext INTEGER)\n
create table attendenceS(roll_num INTEGER PRIMARY KEY,date DATE NOT NULL,status INTEGER NOT NULL)\n
"""
b=a.split("\n")
try:
    while True:
        b.remove('')
except :
    pass
finally:
    print(len(b))

'''
std="""
insert into std_info values
    ('Sarvesh',195001,910619205001,'IT','01-01-2001',1111111111,'north madurai'),
    ('Purnima',195002,910619205002,'IT','01-02-2001',2222222222,'south madurai'),
    ('Amarjeet',195003,910619205003,'IT','01-03-2001',3333333333,'south madurai'),
    ('Sumati',195004,910619205004,'IT','01-04-2001',4444444444,'east madurai'),
    ('Sharma',195005,910619205005,'IT','01-05-2001',5555555555,'west madurai'),
    ('Nagendra',195006,910619205006,'IT','01-06-2001',6666666666,'north madurai'),
"""
imgstdtb="""CREATE TABLE IF NOT EXISTS stimg (roll_num TEX,stbimg BLOB)"""



import sqlite3

c = sqlite3.connect('college-db.db')
cursor = c.cursor()
print("Successfully Connected to SQLite")
# cursor.execute("DROP TABLE stimg")
cursor.execute(imgstdtb)
c.commit()
rno=["195001","195002","195003","195004","195005","195006",]
for i in rno:
    a="temp_/loadstimg/"+i+".png"
    print(a)
    with open(a,'rb') as w:
        t=w.read()
        print(t)
    cursor.execute("INSERT INTO stimg VALUES(?,?)",(i,t))

a=cursor.execute("SELECT * FROM stimg")

for i in a:
    b="temp_/savestimg/"+str(i[0])+".png"
    with open(b,'wb') as f:
        f.write(i[1])
    
cursor.close()


if c:
    c.close()
    print("sqlite connection is closed")

