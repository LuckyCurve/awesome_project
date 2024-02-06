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

        # 创建写入日志的 handler
        fh = logging.FileHandler('../logs/info.log')
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        LOGGER.addHandler(ch)
        LOGGER.addHandler(fh)
        cls._logger = LOGGER
