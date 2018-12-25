#!/usr/bin/env python3

import os
import json
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/news'
db = SQLAlchemy(app)

#def reader(filename):
#    with open('/home/shiyanlou/files/' + filename + '.json','r') as f:
#        return json.load(f)
#
#hs = reader('helloshiyanlou')
#hw = reader('helloworld')

class File(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    content = db.Column(db.Text)

    def __repr__(self):
        return '<File(title=%s)>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))

@app.route('/')
def index():
    #show books list
#    return hs['title'] + ' ' +  hw['title']
    return ''

@app.route('/files/<filename>')
def file(filename):
    #reader content
#    return reader(filename)['content']
    return ''

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
