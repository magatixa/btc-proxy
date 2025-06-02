from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor proxy Brasil Bitcoin online!"

@app.route("/btc")
def btc():
    try:
        url = "https://www.brasilbitcoin.com.br/API/ticker/BTC"
        resposta = requests.get(url)
        data = resposta.json()
        valor_btc = data["ticker"]["last"]
        return str(valor_btc)
    except Exception as e:
        return f"erro: {e}"
