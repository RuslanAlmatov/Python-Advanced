import logging


class ASCIIFilter(logging.Filter):
    def filter(self, record):
        message = record.getMessage()
        return str.isascii(message)
