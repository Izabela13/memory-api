from flask import jsonify, request
from memoryapp import app
from memoryapp.repository import *


@app.route('/categories/<int:category_id>/cards', methods=['GET'])
def cards(category_id):
    return jsonify(get_cards(category_id))


@app.route('/categories/<int:category_id>/cards', methods=['POST'])  # metoda POST,
def add_card(category_id):  # parametr ze ścieżki "category_id" musi znaleźć się w tym miejscu
    r = request.json  # za pomocą obiektu request wyciągamy jscn'a. Przechowujemy to w zmiennej "r".
    # potrzebujemy wyciągnąć słówko i tłumaczenie
    word = r['word']  # wyciągnięte z ciała żądania
    translation = r['translation']  # wartości kluczy, wyciągnięte z ciała żądania

    return jsonify(create_card(category_id, word, translation)), 201  # tworzymy nowy zasób, dlatego zwracamy 201
    # opakowujemy to, co nam wróciło w format JSON.