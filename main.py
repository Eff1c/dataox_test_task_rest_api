import yfinance as yf
from decouple import config
from flask import request
from flask_api import FlaskAPI
from pandas import DataFrame

proxy_server = config('PROXY_SERVER')

app = FlaskAPI(__name__)

def get_history_df(company_name: str) -> DataFrame:
    ticker = yf.Ticker(company_name)
    history_df = ticker.history(period="max", proxy=proxy_server)
    return history_df

@app.route("/", methods=["GET"])
def main():
    company_name = request.data.get('company_name')
    if company_name:
        history_df = get_history_df(company_name)
        orient = request.data.get('orient', default="table")
        history_json = history_df.to_json(orient=orient)
        return history_json
    return {
        "Arguments": "company_name, orient (optional)",
        "Output": "Please input company_name argument!",
        "Options orient": "'columns','records','index','split','table'"
    }
