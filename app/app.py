from flask import Flask, render_template, request, redirect, url_for
from models import db
from flask_migrate import Migrate
# from mysql_db import MySQL

app = Flask(__name__)

application = app
 
app.config.from_pyfile('config.py')

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    query = 'SELECT data from data_table WHERE id = 1'
    cursor = db.connection().cursor(named_tuple=True)
    cursor.execute(query)
    data = cursor.fetchone()
    if data is None:
        status = "Hello, world!"
    else: 
        status = f'Data is: {data.data}'
    return render_template('base.html', status=status)

@app.route('/', methods=['POST'])
def insert():
    print("debug")
    cursor = db.connection().cursor(named_tuple=True)
    query = 'SELECT data from data_table WHERE id = 1'
    cursor.execute(query)
    data = cursor.fetchone()
    if data is None:
        query1 = 'INSERT INTO data_table (id, data) VALUES (1, %s)'
    else:
        query1 = 'UPDATE data_table SET data = %s WHERE id = 1'
    data = request.form.get('data')
    cursor.execute(query1, (data,))
    db.connection().commit()
    cursor.close()
    return redirect(url_for('index'))
