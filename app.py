from flask import Flask, render_template, redirect, url_for, request, send_file
import test
import pandas as pd
app = Flask(__name__)
app.secret_key = "xfwtyAERyuu"

@app.route('/')
def home():
    df = pd.read_csv('nifty50.csv')
    nifty50_data = df.iloc[:, 0].tolist()
    return render_template("home.html", nifty50_data=nifty50_data)

@app.route('/download', methods=["POST", "GET"])
def download():
    if request.method == "POST":
        stock = request.form['stock']
        fromdate = request.form['fromDate']
        todate = request.form['toDate']
        timeframe = request.form['timeFrame']
        test.fetchdata(stock,fromdate,todate,timeframe)
        return send_file('stock_data.xlsx', as_attachment=True)
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
