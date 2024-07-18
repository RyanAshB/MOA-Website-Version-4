from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from flask_mysqldb import MySQL
import mysql.connector


app = Flask(__name__)

db_config = {
    'user': 'root',
    'password': 'password123',
    'host': 'localhost',
    'database': 'food_trade_data'

}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/dbTest')
def dbTest():
    return render_template('dbTest.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    hs_code = request.form['hs_code']
    ie = request.form['placeholder']
    year = request.form['year']

    query_variables = []

    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM food_trade_data WHERE TRUE "

    if hs_code:
        hs_end = ("AND `HS code`= %s")
        query = query + hs_end
        query_variables.append(hs_code)

    if ie:
        ie_end = ("AND `Trade Type`= %s")
        query = query + ie_end
        query_variables.append(ie)


    if year:
        year_end = ("AND `YEAR`= %s")
        query = query + year_end
        query_variables.append(year)

    cursor.execute(query, tuple(query_variables))
    fetchdata = cursor.fetchall()
    cursor.close()
    connection.close()

    return jsonify(fetchdata)



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

