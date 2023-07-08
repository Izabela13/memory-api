# Z pliku __init__ importujemy aplikację
from flask import jsonify  # ta funkcja zamieni listę [] na obiekt/ format JSON
from memoryapp import app  # instancja klasy Flask

# W klasie stworzymy tablicę, która będzie przechowywać kategorie
categories_list = [
    {'category_id': 1,
     'name': 'Dom'},

    {'category_id': 2,
     'name': 'Rodzina'},
]


@app.route('/categories', methods=['GET'])  # ścieżka do zasobów
def categories():
    return jsonify(categories_list)  # metoda zwróci listę w formacie JSON
# Plik "categories" musi zostać zaimportowany do pliku "__init__.py"