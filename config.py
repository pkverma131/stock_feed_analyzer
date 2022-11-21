from datetime import datetime


class Config:

    def __init__(self, opening_time=None, closing_time=None):
        self.opening_time = datetime.strptime(opening_time, '%H:%M:%S').time()
        self.closing_time = datetime.strptime(closing_time, '%H:%M:%S').time()
