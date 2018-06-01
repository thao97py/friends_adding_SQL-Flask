import md5
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')
@app.route('/')
def index():
    friends = mysql.query_db('select * from friends')
    return render_template('index_friend.html', all_friend =friends)
@app.route('/adding', methods= ['POST'])
def create_user():
    query = "INSERT INTO friends (first_name, last_name,occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    occupation= request.form['occupation']
    data = {'first_name': first_name, 'last_name':last_name, 'occupation':occupation}
    mysql.query_db(query, data)
    return redirect ('/')


if __name__ == '__main__':
    app.run(debug=True)