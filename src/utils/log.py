import logging


class LoggerManager:
    _logger = None

    @classmethod
    def get_logger(cls):
        if cls._logger is None:
            cls._init_logger()
        return cls._logger

    @classmethod
    def _init_logger(cls):
        LOGGER = logging.getLogger()
        LOGGER.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        ch.setFormatter(formatter)

        LOGGER.addHandler(ch)
        cls._logger = LOGGER
