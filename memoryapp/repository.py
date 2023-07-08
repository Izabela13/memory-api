""" Plik "repository" to baza danych """

from memoryapp.models import Category


# W klasie stworzymy tablicę, która będzie przechowywać kategorie
# Nigdzie nie ma kontroli błędów - dodajemy konstruktor, do którego przekażemy wartości
categories_list = [
    Category(1, 'Dom'),
    Category(2, 'Rodzina')
]


def get_categories():
    return categories_list