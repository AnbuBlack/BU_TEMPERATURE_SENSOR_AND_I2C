from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from datetime import date, datetime

app = Flask(__name__)#Reference this file
app.config['SQLALCHEMY_DATABASE_URI'] ='sqllite:///test.db' #relative path(///) absolute path(////)
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    content = db.Column(db.String(200), nullable=False)#no want it to be on blamk and save it
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default= datetime.utcnow ) #utcnow  entry created the date will be set automatically


    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')#It is just the name of the file Flask knows how to find it 
    #Template hinheritance 
if(__name__) == '__main__':
    app.run(debug=True) #So if we have any error do not pop up on the website 


