from calendar import month_name
import flask
from  flask import Flask, redirect,render_template,request
import sqlite3

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
  if request.method == 'GET':
       return render_template('index.html')
    
  else:
      
    name=request.form.get('Name')
    month=request.form.get('Month')
    day=request.form.get('Day')
    

    connection=sqlite3.connect('Birthday.db')
    cursor=connection.cursor()
    cursor.execute('INSERT INTO birthday(Name,Month,Day) VALUES(?,?,?)',(name,month,day))
    connection.commit()
    connection.close()
    
    return 'Information stored successfully'