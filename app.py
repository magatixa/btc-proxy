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
        print("Status code:", resposta.status_code)
        print("Conteúdo:", resposta.text)
        return resposta.text  # Mostra o conteúdo real retornado pela API
    except Exception as e:
        return f"erro: {e}"
