from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

#init MySQL
mysql = MySQL(app)


app.config.from_pyfile('config.py')


from views import *

if __name__ == "__main__":
    app.run()