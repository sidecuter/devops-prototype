from flask import Flask, render_template
from mysql_db import MySQL

app = Flask(__name__)

application = app
 
app.config.from_pyfile('config.py')

db = MySQL(app)

@app.route('/')
def index():
    state = f'Connection is {"not " if db.is_connected() else ''}active'
    return render_template('index.html', status=state)
