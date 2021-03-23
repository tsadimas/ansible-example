from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
# app.config['SECRET_KEY'] = os.environ['SECRET_KEY']


db = SQLAlchemy(app)

class students(db.Model):
  id = db.Column('student_id', db.Integer, primary_key = True)
  name = db.Column(db.String(100))
  city = db.Column(db.String(50))
  country = db.Column(db.String(200)) 
 

  def __init__(self, name, city, country):
    self.name = name
    self.city = city
    self.country = country

@app.route('/')
def show_all():
  return render_template('show_all.html', students = students.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
  if request.method == 'POST':
    if not request.form['name'] or not request.form['city'] or not request.form['country']:
      flash('Please enter all the fields', 'error')
    else:
      print(request.form['name'])
      print(request.form['city'])
      print(request.form['country'])

      student = students(request.form['name'], request.form['city'], request.form['country'])
      db.session.add(student)
      db.session.commit()
      flash('Record was successfully added')
      return redirect(url_for('show_all'))
  return render_template('new_student.html')

if __name__ == '__main__':
  db.create_all()
  app.run(debug = True)