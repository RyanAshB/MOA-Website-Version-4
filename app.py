from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from flask_mysqldb import MySQL
import mysql.connector


app = Flask(__name__)

db_config = {
    'user': 'root',
    'password': 'password123',
    'host': 'localhost',
    'database': 'food_import_cleaned'

}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/dbTest')
def dbTest():
    return render_template('dbTest.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    chapter_code = request.form['chapter_code']
    chapter_heading = request.form['chapter_heading']
    result = request.form.getlist('result')
    description = request.form['description']

    params = ', '.join(result)
    query_var = []
    table_headings = []

    connection = get_db_connection()
    cursor = connection.cursor()
    query = f"SELECT {params} FROM food_import_cleaned WHERE TRUE"

    if chapter_code:
        chapter_code_end = (" AND `Chapter code 1`= %s")
        query = query + chapter_code_end
        query_var.append(chapter_code)
        table_headings.append("Chapter Codes")

    if chapter_heading:
        chapter_heading_end = (" AND `Chapter`= %s")
        query = query + chapter_heading_end
        query_var.append(chapter_heading)
        table_headings.append("Chapter Headings")


    if description:
        description_end = (" AND `Description`= %s")
        query = query + description_end
        query_var.append(description)
        table_headings.append("Descriptions")


    cursor.execute(query, tuple(query_var))
    fetchdata = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('results.html', data=fetchdata)
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