from config.config import USER,PASSWD,FIBARO_IP,APP_DEBUG,FILENAME
import base64
import csv

class Credentials():
	def __init__(self):
		self._key=USER+":"+PASSWD

	def getCredentials(self):
		key=base64.b64encode(self._key.encode())
		return key.decode('ascii')

class Url():
	def __init__(self):
		self._url="http://"+FIBARO_IP+"/api/"

	def login(self):
		self._url = self._url+"loginStatus"
		return self._url

	def devices(self):
		self._url = self._url+"devices"
		return self._url

	def sections(self):
		self._url = self._url+"sections"
		return self._url

	def rooms(self):
		self._url = self._url+"rooms"
		return self._url

	def users(self):
		self._url = self._url+"users"
		return self._url

	def panelHistory(self):
		self._url = self._url+"panel/history"
		return self._url

	def energy(self):
		pass

	def temperature(self):
		pass

	def getInfo(self):
		self._url= self._url+"settings/info"
		return self._url


class CSV():
	def __init__(self,flag):
		if(flag==1):
			with open(FILENAME, 'w') as file:
				pass
		else:
			pass

	def read(self):
		pass

	def write(self,data):
		with open(FILENAME, 'a') as file:
			wr = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
			wr.writerow(data)