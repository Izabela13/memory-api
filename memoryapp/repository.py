""" Plik "repository" to baza danych """

from memoryapp.models import Category, Card
from memoryapp.exceptions import NotFoundException


# W klasie stworzymy tablicę, która będzie przechowywać kategorie
# Nigdzie nie ma kontroli błędów - dodajemy konstruktor, do którego przekażemy wartości
categories_list = [
    Category(1, 'Dom'),
    Category(2, 'Rodzina')
]

# Lista na fiszki
cards_list = [
    Card(1, 1, 'Drzwi', 'Door'),
    Card(2, 1, 'Okno', 'Window')
]

# Metoda, która będzie nadawała kolejne numery id
id_categories = 2  # tu trzymamy id
id_cards = 2


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


# Metoda, która na podstawie "category_id" zwróci jakąś kategorię
def get_category(category_id):  # list comprehenisve - przechodzimy przez listę
    # sprawdzamy, czy jakiś "result" został znaleziony
    results = [category for category in categories_list if category.category_id == category_id]
    if results:
        return results[0]  # pobierzemy tylko ten jeden element
    else:
        raise NotFoundException('Category')


# Metoda usuwająca daną kategorię po ID
def delete_category(category_id):
    results = [category for category in categories_list if category.category_id == category_id]

    if results:
        categories_list[:] = [category for category in categories_list if category.category_id != category_id]
        cards_list[:] = [card for card in cards_list if card.category_id != category_id]
    else:
        raise NotFoundException('Category')


# Metoda, która zwróci wszystkie fiszki danej kategorii
def get_cards(category_id):
    print(cards_list)
    categories_results = [category for category in categories_list if category.category_id == category_id]

    if not categories_results:
        raise NotFoundException('Category')

    cards_results = [card for card in cards_list if card.category_id == category_id]

    return cards_results


# Metoda dodająca carty
def create_card(category_id, word, translation):  # 3 parametry
    categories_results = [category for category in categories_list if category.category_id == category_id]
    # Czy w repository mamy taką kategorię? Jeśli tak, przechodzimy do tworzenia fiszki o tej kategorii
    if not categories_results:
        raise NotFoundException('Category')

    card = Card(__next_card_id(), category_id, word, translation) # jeżeli mamy kategorię, tworzymy instancję obiektu klasy
    cards_list.append(card)  # chcemy połączyć fiszkę z kategorią i dodać ją do listy

    return card  # zwracamy nowo utworzoną fiszkę (i wracamy do kontrolera z fiszkami)


def __next_card_id(): # ta funkcja będzie nam zmieniać id dla fiszki (card)
    global id_cards
    id_cards += 1
    return id_cards


# Metoda do usuwania fiszek
def delete_card(category_id, card_id):
    categories_results = [category for category in categories_list if category.category_id == category_id]

    if not categories_results:
        raise NotFoundException('Category')

    cards_result = [card for card in cards_list if card.category_id == category_id and card.card_id == card_id]

    if cards_result:
        cards_list[:] = [card for card in cards_list if card.category_id != category_id or card.card_id != card_id]
    else:
        raise NotFoundException('Card')
