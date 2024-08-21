from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)

db_config = {
    'user': 'root',
    'password': 'password123',
    'host': 'localhost',
    'database': 'overseas_importers'

}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/jacra')
def jacra():
    return render_template('jacra.html')

@app.route('/2025')
def twenty():
    return render_template('2025.html')

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/export-animals')
def export_animals():
    return render_template('export-animals.html')

@app.route('/banana-board')
def banana_board():
    return render_template('banana-board.html')

@app.route('/international-market')
def international_market():
    return render_template('international-market.html')

@app.route('/domestic-market')
def domestic_market():
    return render_template('domestic-market.html')

@app.route('/investment-crops')
def investment_crops():
    return render_template('investment-crops.html')

@app.route('/aquaculture')
def aquaculture():
    return render_template('aquaculture.html')

@app.route('/resources')
def resource():
    return render_template('resources.html')

@app.route('/overseas')
def overseas():
    return render_template('overseas.html')

@app.route('/trade-agreements')
def trade_agreements():
    return render_template('trade-agreements.html')

@app.route('/overseas_form', methods=['POST'])
def overseas_form():
    commodity = request.form['commodity']

    connection = get_db_connection()
    cursor = connection.cursor()

    query = "SELECT Country, Name_of_Company, Address, Address_Continued, Contact_Information FROM overseas_importers WHERE Commodity=%s"

    cursor.execute(query, (commodity,))
    fetchdata = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('overseas-results.html', data=fetchdata)




if __name__ == '__main__':
    app.run(debug=True)










# def get_db_connection():
#     return mysql.connector.connect(**db_config)

# @app.route('/dbTest')
# def dbTest():
#     return render_template('dbTest.html')

# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     hs_code = request.form['hs_code']
#     ie = request.form['placeholder']
#     year = request.form['year']

#     query_variables = []

#     connection = get_db_connection()
#     cursor = connection.cursor()
#     query = "SELECT * FROM food_trade_data WHERE TRUE "

#     if hs_code:
#         hs_end = ("AND `HS code`= %s")
#         query = query + hs_end
#         query_variables.append(hs_code)

#     if ie:
#         ie_end = ("AND `Trade Type`= %s")
#         query = query + ie_end
#         query_variables.append(ie)


#     if year:
#         year_end = ("AND `YEAR`= %s")
#         query = query + year_end
#         query_variables.append(year)

#     cursor.execute(query, tuple(query_variables))
#     fetchdata = cursor.fetchall()
#     cursor.close()
#     connection.close()

#     return jsonify(fetchdata)