from utils import string_to_time


class QuoteInfo:
    def __init__(self, config, trade_date, trade_time, symbol, price):
        self.config = config
        self.symbol = symbol
        self.trade_date = trade_date
        self.trade_time = trade_time
        self.price = price

    def validate(self):
        return self.config.opening_time <= string_to_time(self.trade_time) <= self.config.closing_time


class QuoteRegister:

    def __init__(self, quote_adapter):
        self.quote_adapter = quote_adapter

    def add_quote(self, quote):
        if quote not in self.quote_adapter:
            self.quote_adapter.append(quote)

    def get_registered_quotes(self):
        return self.quote_adapter

