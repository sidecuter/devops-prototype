from flask import Flask, render_template, request, redirect, url_for
from mysql_db import MySQL

app = Flask(__name__)

application = app
 
app.config.from_pyfile('config.py')

db = MySQL(app)

@app.route('/')
def index():
    query = 'SELECT data from data_table WHERE id = 1'
    cursor = db.connection().cursor(named_tuple=True)
    cursor.execute(query)
    data = cursor.fetchone()
    status = f'Data is: {data}'
    return render_template('base.html', status=status)

@app.route('/', methods=['POST'])
def insert():
    query = 'UPDATE data_table SET data = %s WHERE id = 1'
    data = request.form.get('data')
    cursor = db.connection().cursor(named_tuple=True)
    cursor.execute(query, (data,))
    db.connection().commit()
    cursor.close()
    return redirect(url_for('index'))
