import logging

class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info(
            "Setting {k} to {v}".\
            format(k=key, v=value))
        return super(LoggingDict, self).\
        __setitem__(key, value)

logging.basicConfig(level=logging.INFO)

ld = LoggingDict()
ld["a"] = 123
