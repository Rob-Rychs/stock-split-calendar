class Record:
    def __init__(self, name, symbol, country, factor, date):
        self.name = name
        self.symbol = symbol
        self.country = country
        self.factor = factor
        self.date = date

    def __str__(self):
        return self.name + \
               ' ' * (40 - len(self.name)) + \
               self.symbol + \
               ' ' * (20 - len(self.symbol)) + \
               self.country + \
               ' ' * (20 - len(self.country)) + \
               self.factor + \
               ' ' * (20 - len(self.factor)) + \
               self.date
