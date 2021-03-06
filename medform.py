#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: kayfindo
"""
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('medform.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      with open('file.json', 'w') as f:
        json.dump(request.form, f)
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)