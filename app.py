from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from flask_mysqldb import MySQL
import mysql.connector
import pandas as pd
import openpyxl
from fileinput import filename

app = Flask(__name__)

db_config = {
    'user': 'root',
    'password': 'password123',
    'host': 'localhost',
    'database': 'overseas_importers'

}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/dbTest')
def dbTest():
    return render_template('dbTest.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    print("Attempt 9")
    file = request.files['my_file']
    df = pd.read_excel(file)
    df.columns = df.columns.str.strip()

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS overseas_importers;")
    cursor.execute("CREATE TABLE overseas_importers (Commodity varchar(255), Country varchar(255), Name_of_Company varchar(255), Address varchar(255), Address_Continued varchar(255));")

    for index, row in df.iterrows():

        values = [
            row['Commodity'] if pd.notna(row['Commodity']) else None,
            row['Country'] if pd.notna(row['Country']) else None,
            row['Name of Company'] if pd.notna(row['Name of Company']) else None,
            row['Address'] if pd.notna(row['Address']) else None,
            row.get("Address Cont'd") if pd.notna(row.get("Address Cont'd")) else None
        ]

        cursor.execute(
            "INSERT INTO overseas_importers (Commodity, Country, Name_of_Company, Address, Address_Continued) VALUES (%s, %s, %s, %s, %s)",
            values
        )

    conn.commit()
    cursor.close()
    conn.close()
    
    return render_template('dbTest.html')
    

    # conn = get_db_connection()
    # cursor = conn.cursor()

    # for index, row in df.iterrows():
    #     cursor.execute(
    #         "INSERT INTO importers (Commodity, Country, Name_of_Company, Address, Address_Contd) VALUES (%s, %s, %s, %s, %s)",
    #         (row['Commodity'], row['Country'], row['Name of Company'], row['Address'], row['Address Contd'])
    #     )
    # conn.commit()
    # cursor.close()
    # conn.close()

    # return "Effort"
    
    # hs_code = request.form['hs_code']
    # ie = request.form['placeholder']
    # year = request.form['year']

    # query_variables = []

    # connection = get_db_connection()
    # cursor = connection.cursor()
    # query = "SELECT * FROM food_trade_data WHERE TRUE "

    # if hs_code:
    #     hs_end = ("AND `HS code`= %s")
    #     query = query + hs_end
    #     query_variables.append(hs_code)

    # if ie:
    #     ie_end = ("AND `Trade Type`= %s")
    #     query = query + ie_end
    #     query_variables.append(ie)


    # if year:
    #     year_end = ("AND `YEAR`= %s")
    #     query = query + year_end
    #     query_variables.append(year)

    # cursor.execute(query, tuple(query_variables))
    # fetchdata = cursor.fetchall()
    # cursor.close()
    # connection.close()

    # return jsonify(fetchdata)



@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/hte')
def hte():
    return render_template('hte.html')

@app.route('/queries')
def queries():
    return render_template('queries.html')

@app.route('/landing-page')
def landing():
    return render_template('landing-page.html')

@app.route('/2025')
def twenty_five():
    return render_template('2025.html')

@app.route('/results')
def results():
    return render_template('results.html')



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