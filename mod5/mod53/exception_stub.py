class BlockError:
    def __init__(self, error):
        self.error = error

    def __enter__(self):
        pass

    def __exit__(self, type, val, traceback):
        if (type is not None) and (type not in self.error):
            raise val
        return True