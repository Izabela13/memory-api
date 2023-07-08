""" Plik "repository" to baza danych """

# W klasie stworzymy tablicę, która będzie przechowywać kategorie
categories_list = [
    {'category_id': 1,
     'name': 'Dom'},

    {'category_id': 2,
     'name': 'Rodzina'},
]


def get_categories():
    return categories_list