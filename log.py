from email import message
import logging
# logging.basicConfig(filename='log.txt', level=logging.WARNING)
# how to formate logging message
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y %I:%m:%S')
print('logginig modules demo')
logging.debug('debug info')
logging.info('info informations')
logging.warning('waring info')
logging.error('error info')
logging.critical('critical info')


