import json
from os.path import abspath, isfile
import sys

json_path = abspath("./config.json")

try:
	with open(json_path) as json_data:
		data = json.load(json_data)
except Exception as e:
	print('Failed to init')
	print(e)
	sys.exit()

FIBARO_IP = data['app']['fibaro_ip']

APP_DEBUG = data['app']['debug']

USER = data['app']['username']

PASSWD = data['app']['password']

FILENAME = data['data']['filename']