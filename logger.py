import logging

logging.basicConfig(filename='system_log.txt', level=logging.INFO, format='%(asctime)s_%(message)s', datefmt='%d/%m/%Y_%H:%M')

def log_event(event):
    logging.info(event)