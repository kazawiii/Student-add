import sqlite3

db_local = 'student.db'
cnxn = sqlite3.connect(db_local)
c = cnxn.cursor()

c.execute("""
create table contact_details 
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
FISRT_NAME TEXT,
LAST_NAME TEXT  ,
ADDRESS TEXT 
)
""")

cnxn.commit()
cnxn.close()