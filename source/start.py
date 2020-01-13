import client
import logfile

if __name__ == "__main__":
    logger = logfile.somewhere_logger()
    logger.somewhere_info("main start!")
    instance = client.Client()
    instance.start()