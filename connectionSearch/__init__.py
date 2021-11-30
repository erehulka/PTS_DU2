import logging

logging.basicConfig(filename='./log/exception.log', format='%(asctime)s %(levelname)s - %(name)s: %(message)s',
                    datefmt='%d.%m.%Y %H:%M:%S', level=logging.INFO)
