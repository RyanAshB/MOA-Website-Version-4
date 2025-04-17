from flask import Flask, render_template, request, jsonify
 
app = Flask(__name__)

@app.route('/')
def base():
    return render_template('landing.html')

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


if __name__ == "__main__":
    app.run(debug=True)

# To run project locally
# waitress-serve --listen=127.0.0.1:5000 app:app

# Packages removed
# Flask-MySQLdb==2.0.0
# mysql-connector-python==9.2.0
# mysqlclient==2.2.7


# Docker to Build Image
# docker build -t trade-portal:1.0.0 .

# Docker to run container
# docker run  -p 5000:5000 --name TradePortal trade-portal:1.0.0