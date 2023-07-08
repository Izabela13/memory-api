class NotFoundException(Exception):  # nasz wyjątek będzie rozszerzał klasę "Exception"
    def __init__(self, item):  # chcemy, aby w naszym konstruktorze był jeszcze przekazywany "item"
        self.item = item  # przekazujemy do parametru "item" poszukiwaną kategorię.