from flask import Flask
import requests

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
        valor_btc_usd = data["quotes"]["USD"]["price"]
        return str(valor_btc_usd)
    except Exception as e:
        return f"erro: {e}"
