from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Proxy CoinPaprika ativo"

@app.route("/btc")
def btc():
    try:
        url = "https://api.coinpaprika.com/v1/tickers/btc-bitcoin"
        resposta = requests.get(url)
        data = resposta.json()
        # Para debug, mostra o JSON completo
        return "<pre>" + json.dumps(data, indent=2) + "</pre>"
    except Exception as e:
        return f"erro: {e}"
