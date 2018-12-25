#!/usr/bin/env python3

import os
import json
from flask import Flask, render_template

app = Flask(__name__)

def reader(filename):
    with open('/home/shiyanlou/files/' + filename + '.json','r') as f:
        return json.load(f)

hs = reader('helloshiyanlou')
hw = reader('helloworld')

@app.route('/')
def index():
    #show books list
    return hs['title'] + ' ' +  hw['title']

@app.route('/files/<filename>')
def file(filename):
    #reader content
    return reader(filename)['content']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
