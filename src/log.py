import os
import platform
from datetime import datetime
from datetime import date

# Arquivo para gravar o log nos arquivos

# Verificação se a plataforma é Linux ou outro
path_log = '/tmp/logs/log_'
if(platform.system() not in ['Linux', 'Darwin']):
	path_log = '\\tmp\\logs\\log_'

# Grava mensagens no LOG do sistema (arquivo logs/log_ANO-MES-DIA.log)
def register(level, msg):
	if not os.path.exists('tmp/logs'):
		os.makedirs('tmp/logs')
	with open(os.path.dirname(os.path.realpath(__file__)) + path_log + str(date.today()) + '.log', 'a', encoding='utf-8') as log_file:
		log_file.write("[{}] {}: {} \n".format(str(datetime.now()), level, msg))

def error(origin, msg):
	register('ERROR', origin + ": " + msg)

def info(origin, msg):
	register('INFO', origin + ": " + msg)

def debug(origin='', msg=''):
	register('DEBUG', origin + ": " + msg)