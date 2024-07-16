from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os


app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/hte-ackee')
def ackee():
    return render_template('hte-ackee.html')

@app.route('/queries')
def queries():
    return render_template('queries.html')

@app.route('/landing-page')
def landing():
    return render_template('landing-page.html')

@app.route('/2025')
def twenty_five():
    return render_template('2025.html')



if __name__ == '__main__':
    app.run(debug=True)

