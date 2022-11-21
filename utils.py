from datetime import datetime

VALID_QUOTE_ATTRIBUTE_COUNT = 4


def valid_quote(quote):
    return VALID_QUOTE_ATTRIBUTE_COUNT == len(quote)


def string_to_time(string):
    # print(string)
    return datetime.strptime(string, '%H:%M:%S').time()
