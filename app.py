from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor proxy CoinDesk online!"

@app.route("/btc")
def btc():
    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice/BRL.json"
        headers = {"User-Agent": "Mozilla/5.0"}
        resposta = requests.get(url, headers=headers)
        data = resposta.json()
        valor_btc = data["bpi"]["BRL"]["rate_float"]
        return str(valor_btc)
    except Exception as e:
        return f"erro: {e}"
