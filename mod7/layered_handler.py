import logging


class LayredHandler(logging.Handler):
    def __init__(self):
        super().__init__()

        self.handlers = {
            logging.DEBUG: logging.FileHandler("calc_debug.log"),
            logging.INFO: logging.FileHandler("calc_info.log"),
            logging.WARNING: logging.FileHandler("calc_warning.log"),
            logging.ERROR: logging.FileHandler("calc_error.log"),
            logging.CRITICAL: logging.FileHandler("calc_critical.log"),
        }
        self.formatter = logging.Formatter("%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s")

    def emit(self, record):
        handler = self.handlers.get(record.levelno)
        if handler:
            handler.setFormatter(self.formatter)
            handler.emit(record)
