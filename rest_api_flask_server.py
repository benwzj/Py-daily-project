from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
import pymysql
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()

CORS(app)

# Setup database connection
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Gbca-123'
app.config['MYSQL_DATABASE_DB'] = 'careertraining'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@auth.verify_password
def authenticate(username, password):
    if username == "GBCA" and password == "abc!!":
        return True
    else:
        return False


def format_response(data, status_code=200):
    response = jsonify(data)
    response.status_code = status_code
    return response


@app.route('/students')
def get_students():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select studentid, student_name, mobile from students")
        rows = cursor.fetchall()
        return format_response(rows)

    except pymysql.Error as e:
        return format_response(e.args[1], 400)


@app.route('/students/<int:studentid>')
def get_one_student(studentid):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = f"select studentid, student_name, mobile from students where studentid = {studentid}"
        affected_row = cursor.execute(sql)
        if affected_row == 1:
            row = cursor.fetchone()
            return format_response(row)
        else:
            return format_response("Invalid student id.", 404)
        
    except pymysql.Error as e:
        return format_response(e.args[1], 400)


@app.route('/students', methods = ['POST']  )
@auth.login_required
def add_student():
    new_student  = request.json
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = f"insert into students (studentid, student_name, mobile ) values ( {new_student.get('studentid')}, '{new_student.get('student_name')}', '{new_student.get('mobile')}')"

        affected_row = cursor.execute(sql)
        conn.commit()
        
        if affected_row == 1:
            return format_response("Student added successfully")
        else:
            return format_response("Insert error", 404)
        
    except pymysql.Error as e:
        return format_response(e.args[1], 400)


@app.route('/students/<int:studentid>', methods = ['DELETE'])
@auth.login_required
def delete_student(studentid):
            
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = f"delete from students where studentid = {studentid}"
  
        affected_row = cursor.execute(sql)
        conn.commit()
        
        if affected_row == 1:
            return format_response("Student deleted successfully.")
        else:
            return format_response("Delete error", 404)
        
    except pymysql.Error as e:
        return format_response(e.args[1], 400)


@app.route('/students', methods = ['PUT']  )
@auth.login_required
def update_student():
    update_student  = request.json

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = f"update students set student_name = '{update_student.get('student_name')}', mobile = {update_student.get('mobile')} where studentid = {update_student.get('studentid')} "

        affected_row = cursor.execute(sql)
        conn.commit()
        
        if affected_row == 1:
            return format_response("Student updated successfully.")
        else:
            return format_response("Not updated", 404)
        
    except pymysql.Error as e:
        return format_response(e.args[1], 400)


app.run(host='localhost', port=3001)