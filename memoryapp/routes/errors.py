"""Plik wyłapujący wyjątki"""

from flask import jsonify  # żeby zamieniało pliki do JSON

from memoryapp import app
from memoryapp.exceptions import NotFoundException


@app.errorhandler(NotFoundException) # oczekuje, żeby przekazać klasę wyjątków, które ma wyłapywać
def handle_not_found(e: NotFoundException):  # ten wyjątek, który znajdzie się w innym miejscu, będzie pod zmienną "e"
    return jsonify({'message': f'{e.item} not found'}), 404
    #zwracamy obiekt, który będzie reprezentował odpowiedź
    # kod błędu 400 --> błąd po stronie klienta
