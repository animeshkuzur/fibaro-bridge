import json
from os.path import join, dirname, isfile
import sys

json_path = join(dirname(__file__), "config.json")
json_path = join("../",json_path)

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