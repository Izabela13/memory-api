# Tworzymy klasę, która będzie zawierała same pola

from dataclasses import dataclass  # chcemy zadekorować klasę jako "klasę danych"
from dataclasses_json import dataclass_json  # implementacja metod odpowiadających za konwersję do JSON'a


# Kolejność dekoratorów ma znaczenie. W pierwszej kolejności musi pojawić się @dataclass_json
@dataclass_json
@dataclass
class Category:
    category_id: int
    name: str

# W repozytorium zamieniamy obiekty w "category_list"


# Deklarowanie pól (pola to właściwości naszej klasy)
@dataclass_json
@dataclass
class Card:
    card_id: int
    category_id: int
    word: str
    translation: str

