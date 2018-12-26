#!/usr/bin/env python3
# -*- coding:utf-8-*-

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
    category = db.relationship('Category')

    def __init__(self,title,created_time,category,content):
        self.title  = title
        self.created_time = created_time
        self.content = content
        self.category = category

    def __repr__(self):
        return '<File(title=%s)>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return '<Category(name=%s)>' % self.name

@app.route('/')
def index():
    #show books list
#    return hs['title'] + ' ' +  hw['title']
    files = File.query.all()
    file_titles = {} 
    for fil in files:
        file_titles[fil.id] = fil.title
    return render_template('index.html',file_titles=file_titles)

@app.route('/files/<file_id>')
def file(file_id):
    #reader content
#    return reader(filename)['content']
    fileobj = File.query.filter_by(id=file_id).first()
    file_list = [fileobj.content,str(fileobj.created_time),fileobj.category.name]
#    for i in iter(file_list):
#        print(i)
    return render_template('file.html',file_list=file_list)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
