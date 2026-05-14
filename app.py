'''
from flask import Flask, request

app= Flask (__name__)

@app.route('/')
def home():                            
    return 'Hello user! This is my first flask app'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/contact')
def contact():
    return 'This is the contact page'

@app.route('/submit' , methods=["GET","POST"])
def submit():
    if request.method == "POST":
        return "You sent data"
    else:
        return "You are the viewing the form"


'''
