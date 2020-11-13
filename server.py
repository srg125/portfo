# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:32:39 2020

@author: Sophie
"""
from flask import Flask, render_template, request, redirect
import csv

# instantiate an app
app = Flask(__name__)

# htmls need to be in folder called templates
# CSS and javascript need to be in folder called static


@app.route('/') # if hit /, define and call function 
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>') 
def html_page(page_name):
    return render_template(page_name)

# for contact form
def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode = 'a', newline = '') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter = ',', quotechar = '"',
                                quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again.'
    


