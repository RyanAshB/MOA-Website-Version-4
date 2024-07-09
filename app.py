from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=True)

