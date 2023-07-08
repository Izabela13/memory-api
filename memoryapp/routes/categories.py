from flask import jsonify, request  # ta funkcja zamieni listę [] na obiekt/ format JSON
from memoryapp import app  # instancja klasy Flask
from memoryapp.repository import *  # import metod z pliku "repository"


@app.route('/categories', methods=['GET'])  # ścieżka do zasobów
def categories():
    return jsonify(get_categories())  # metoda zwróci listę w formacie JSON
# Plik "categories" musi zostać zaimportowany do pliku "__init__.py"

"""
JSON zamienia obiekty pythonowe na format tekstowy
"""


@app.route('/categories', methods=['POST'])
def add_category():  # przekazywanie do repozytorium kategrii. Musimy ją wysłać w formacie JSON
    r = request.json  # obiekt, który będzie przekazywany
    category_name = r['name']  # z naszego żądania, które jest w formacie JSON będziemy wyciągać klucz zmiennej

    return jsonify(create_category(category_name)), 201  # "category_name" to żądanie
    # ciało odpowiedzi + kod odpowiedzi


@app.route('/categories/<int:category_id>', methods=['GET'])  # "int:category_id" konwersja do typu int
def category(category_id):  # nazwa musi być identyczna jak z routa
    return jsonify(get_category(category_id))