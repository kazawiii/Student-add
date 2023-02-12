import sqlite3

db_local = 'student.db'
cnxn = sqlite3.connect(db_local)
c = cnxn.cursor()

c.execute("""
select * from   CONTACT_DETAILS
""")
student_info = c.fetchall()
for i in student_info:
    print(i)



cnxn.commit()
cnxn.close()