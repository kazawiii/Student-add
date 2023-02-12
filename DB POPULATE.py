import sqlite3

db_local = 'student.db'
cnxn = sqlite3.connect(db_local)
c = cnxn.cursor()

c.execute("""
INSERT INTO CONTACT_DETAILS (FISRT_NAME,LAST_NAME,ADDRESS) VALUES
('NABIL','KINANE','PROVIDENCE'),
('NAJIB','KINANE','FRANCE'),
('OTHMAN','KINANE','CASA'),
('SAADIA','KINANE','BENAHMED')
""")

cnxn.commit()
cnxn.close()