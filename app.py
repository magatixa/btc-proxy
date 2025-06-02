from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor proxy CoinGecko online!"

@app.route("/btc")
def btc():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"
        resposta = requests.get(url)
        data = resposta.json()
        valor_btc = data["bitcoin"]["brl"]
        return str(valor_btc)
    except Exception as e:
        return f"erro: {e}"
