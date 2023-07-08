from flask import Flask
from flask_cors import CORS


# Instancja klasy Flask
app = Flask(__name__)  # nazwa domyślnego pakietu
cors = CORS(app, resources={r"/*": {"origins": "*"}})  # r"" - oznacza, że jest to format "row"
app.debug = True  # W terminalu wyświetli się każde odpytanie, które trafiać będzie do aplikacji


"""
ZMNIEJSZENIE RESTRYKCJI
{"origins": "*"}} - obojętnie, z jakiego źródła będzie pochodziło zapytanie, serwer będzie przepuszczał
"""

import memoryapp.routes