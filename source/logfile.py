import logging
import logging.handlers

class somewhere_logger():

    LOG_FILE = 'somewhere_py_client.log'
    handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)
    fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)

    logger = logging.getLogger('somewhere')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    def somewhere_debug(self, *msg):
        self.logger.debug(msg)

    def somewhere_info(self, *msg):
        self.logger.info(msg)

    def somewhere_warning(self, *msg):
        self.logger.warning(msg)

    def somewhere_error(self, *msg):
        self.logger.error(msg)

    def somewhere_critical(self, *msg):
        self.logger.critical(msg)


