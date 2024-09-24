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

@app.route('/export-plants')
def export_plants():
    return render_template('export-plants.html')

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
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "DESCRIBE overseas_importers;"
    cursor.execute(query, )

    headings=[]
    headingdata = cursor.fetchall()
    for i in headingdata:
        headings.append(i[0].replace("_", " "))

     
    query = f"SELECT DISTINCT {headings[0]} FROM overseas_importers"
    cursor.execute(query, )
    distinct_commodities = cursor.fetchall()

    main_commodities = []
    for distinct in distinct_commodities:
        main_commodities.append(distinct[0])
    print(main_commodities)

        
    cursor.close()
    connection.close()
    return render_template('overseas.html', main_commodities=main_commodities)



@app.route('/trade-agreements')
def trade_agreements():
    return render_template('trade-agreements-v2.html')

@app.route('/training')
def training():
    return render_template('training.html')

@app.route('/market-research')
def market_research():
    return render_template('market-research.html')

@app.route('/sps-tbt')
def sps_tbt():
    return render_template('sps-tbt.html')

@app.route('/overseas_form', methods=['GET', 'POST'])
def overseas_form():
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "DESCRIBE overseas_importers;"
    cursor.execute(query, )

    headings=[]
    headingdata = cursor.fetchall()
    for i in headingdata:
        headings.append(i[0].replace("_", " "))

     
    query = f"SELECT DISTINCT {headings[0]} FROM overseas_importers"
    cursor.execute(query, )
    distinct_commodities = cursor.fetchall()

    main_commodities = []
    for distinct in distinct_commodities:
        main_commodities.append(distinct[0])
    print(main_commodities)

    fetchdata = []
    
    if request.method == 'POST':
        commodity = request.form['commodity']


        query = "SELECT * FROM overseas_importers WHERE Commodity LIKE %s"
        cursor.execute(query, ('%' + commodity + '%',))
        fetchdata = cursor.fetchall()
        
    cursor.close()
    connection.close()

    return render_template('overseas-results.html', data=fetchdata, headings=headings, main_commodities=main_commodities)





if __name__ == '__main__':
    app.run(debug=True)
