from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
import pymysql
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()

CORS(app)

username = 'root'
mysql_pass = 'Gbca-123'
mysql_db = 'classicmodels'
mysql_host = 'localhost'

# Setup database connection
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = username
app.config['MYSQL_DATABASE_PASSWORD'] = mysql_pass
app.config['MYSQL_DATABASE_DB'] = mysql_db
app.config['MYSQL_DATABASE_HOST'] = mysql_host
mysql.init_app(app)


# @auth.verify_password
# def authenticate(username, password):
#     if username == "GBCA" and password == "abc!!":
#         return True
#     else:
#         return False


def format_response(data, status_code=200):
    response = jsonify(data)
    response.status_code = status_code
    return response

@app.route('/employees')
def get_employees():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from employees")
        rows = cursor.fetchall()
        return format_response(rows)

    except pymysql.Error as e:
        return format_response(e.args[1], 400)
    

@app.route('/employee/<int:employeenumber>')
def get_employee(employeenumber):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = f"select * from employees where employeeNumber = {employeenumber}"
        affected_row = cursor.execute(sql)
        if affected_row == 1:
            row = cursor.fetchone()
            return format_response(row)
        else:
            return format_response("Invalid employee number.", 404)
        
    except pymysql.Error as e:
        return format_response(e.args[1], 400)

@app.route('/employees', methods = ['POST']  )
# @auth.login_required
def add_employee():
    new_employee  = request.json
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = f"insert into employees (employeeNumber, lastName, firstName, email, jobTitle, officeCode) values ( {new_employee.get('employeeNumber')}, '{new_employee.get('lastName')}', '{new_employee.get('firstName')}', {new_employee.get('email')}, {new_employee.get('jobTitle')}, {new_employee.get('officeCode')})"

        affected_row = cursor.execute(sql)
        conn.commit()
        
        if affected_row == 1:
            return format_response("employee added successfully")
        else:
            return format_response("Insert error", 404)
        
    except pymysql.Error as e:
        return format_response(e.args[1], 400)
    
@app.route('/customers')
def get_customers():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from customers")
        rows = cursor.fetchall()
        return format_response(rows)

    except pymysql.Error as e:
        return format_response(e.args[1], 400)


@app.route('/customer/<int:customernumber>')
def get_customer(customernumber):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = f"select * from customers where customerNumber = {customernumber}"
        affected_row = cursor.execute(sql)
        if affected_row == 1:
            row = cursor.fetchone()
            return format_response(row)
        else:
            return format_response("Invalid customer number.", 404)
        
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