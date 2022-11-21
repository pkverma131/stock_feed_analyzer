from reader import FeadReader
from quote import QuoteInfo, QuoteRegister
from config import Config

config = Config(opening_time='09:30:00', closing_time='16:30:00')


class Application:
    # def __int__(self, file_name):
    #     self.file_name = file_name
    #     self.feed_text = None

    def analyze_feed(self, feed):
        """
        :rtype: object

        """
        print('reading feed')


if __name__ == '__main__':
    fr = FeadReader('stock_feed.csv')
    feeds = fr.get_feeds()
    print(feeds)
    # app = Application('stock_feed.csv')
    # app.analyze_feed()
    quote_reg = QuoteRegister([])
    for feed in feeds:
        quote = QuoteInfo(config, feed['trade_date'], feed['trade_time'], feed['symbol'], feed['price'])
        if quote.validate():
            print('yes')
            quote_reg.add_quote(quote)
    print (quote_reg.get_registered_quotes())

