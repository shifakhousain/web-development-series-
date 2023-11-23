from flask import Flask, render_template, request, session, url_for
from flask_mysql import MySQL
import mysql.connector 
import passlib.hash 
from wtforms import Form, Stringfield, Emailfield, Passwordfield 


app = Flask(__name__)

app.config['MySQL_HOST'] = 'localhost'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = ''
app.config['MySQL_DB'] = 'userinfo2'

mysql = MySQL(app)





@app.route('/day1')
def day1():
	return render_template('day1.html')

@app.route('/')
def day2():
	return render_template('day2.html')

@app.route('/day3')
def day3():
	return render_template('day3.html')

@app.route('/signup')
def day4():
	return render_template('day4.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']


        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO users VALUES(%s,%s,%s,%s)''',(name,username,email,password))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
 
app.run(host='localhost', port=5000)


if __name__ == '__main__':
	app.run(debug=True)
