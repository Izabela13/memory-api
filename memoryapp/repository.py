""" Plik "repository" to baza danych """

from memoryapp.models import Category


# W klasie stworzymy tablicę, która będzie przechowywać kategorie
# Nigdzie nie ma kontroli błędów - dodajemy konstruktor, do którego przekażemy wartości
categories_list = [
    Category(1, 'Dom'),
    Category(2, 'Rodzina')
]

# Metoda, która będzie nadawała kolejne numery id
id_categories = 2 # tu trzymamy id


def get_categories():
    return categories_list


# Metoda, która będzie tworzyła nową kategorię
def create_category(category_name):  # oczekujemy przekazania nowej nazwy (czyli, "category_name")
    category = Category(__next_category_id(),   # nowy obiekt klasy kategorii + skorzystanie z metody numerującej id
                        category_name)
    categories_list.append(category)  # dodajemy do listy kategorii ("categories_list") nowo utworzoną kategorię
    return category  # zwrócenie numeru id nowej kategorii


# Metoda prywatna nadająca kolejne numery id
def __next_category_id():
    global id_categories # Po dodaniu "global" globalną zmienną możemy modyfikować. Bez tego mamy do czynienia ze zmienną lokalną
    id_categories += 1  # zwiększamy liczbę, którą przechowuje zmienna "id_categories"
    return id_categories  # zwracanie wartości "id_categories".