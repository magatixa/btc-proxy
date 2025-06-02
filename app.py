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
        print(data)  # Para log no Render
        return str(data)  # Retorna o JSON completo
    except Exception as e:
        return f"erro: {e}"
