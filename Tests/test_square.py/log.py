#import du module logging (bibliothèque)
import logging
# définition du fichier de log  et son niveau de sensibilité
logging.basicConfig(filename='testing_log.log',level=logging.DEBUG,\
      format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')
logging.debug('Debug error')
logging.info('INFO ERROR')
logging.warning('Warning Error %s: %s', '01234', 'Erreur objet')
logging.error('error message')
logging.critical('critical error')