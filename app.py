from flask import Flask, render_template , request
import sqlite3


app = Flask(__name__)
db_local = 'student.db'


@app.route('/')
@app.route('/Home')
def homepage():
    student_data = query_contact_details()
    return render_template('home.html', student_data=student_data)


def query_contact_details():
    cnxn = sqlite3.connect(db_local)
    c = cnxn.cursor()

    c.execute("""
    select * from   CONTACT_DETAILS
    """)
    student_data = c.fetchall()
    return student_data


@app.route('/add', methods=['GET', 'POST'])
def addstudent():
    if request.method == 'GET':
        return render_template('add_student.html')
    else:
        student_detail= (
            request.form['firstname'],
            request.form['lastname'],
            request.form['address']

        )
        insert_student(student_detail)
        return render_template('add_success.html')

def insert_student(student_detail):
    cnxn = sqlite3.connect(db_local)
    c = cnxn.cursor()
    sql = 'insert into   CONTACT_DETAILS (FISRT_NAME,last_name,address) values(?,?,?)'
    c.execute(sql, student_detail)
    cnxn.commit()
    cnxn.close()


if __name__ == '__main__':
    app.run()
