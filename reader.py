from utils import valid_quote


class FeadReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_feeds(self):
        feeds = []
        data = open(self.file_name, 'r')
        lines = data.read().splitlines()
        for line in lines:
            feed = line.split(',')
            if valid_quote(feed):
                feeds.append({'trade_date': feed[0], 'trade_time': feed[1],
                              'symbol': feed[2], 'price': feed[3]})
        return feeds


