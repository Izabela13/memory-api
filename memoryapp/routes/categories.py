from flask import jsonify  # ta funkcja zamieni listę [] na obiekt/ format JSON
from memoryapp import app  # instancja klasy Flask
from memoryapp.repository import *  # import metod z pliku "repository"


@app.route('/categories', methods=['GET'])  # ścieżka do zasobów
def categories():
    return jsonify(get_categories())  # metoda zwróci listę w formacie JSON
# Plik "categories" musi zostać zaimportowany do pliku "__init__.py"

"""
JSON zamienia obiekty pythonowe na format tekstowy
"""