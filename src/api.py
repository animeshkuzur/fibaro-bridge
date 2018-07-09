from config.config import FIBARO_IP,APP_DEBUG,USER,PASSWD
from src.api_request import API_Request
from src.utils import Url

class API():
	def __init__(self):
		# self._params = {}
		self._api=API_Request()
		
	def getLoginStatus(self):
		params = {}
		url=Url()
		response=self._api.GET(url.login(),params)
		return response

	def getDevices(self):
		params = {}
		url=Url()
		response=self._api.GET(url.devices(),params)
		return response

	def getSections(self):
		params = {}
		url=Url()
		response=self._api.GET(url.sections(),params)
		return response

	def getRooms(self):
		params = {}
		url=Url()
		response=self._api.GET(url.rooms(),params)
		return response

	def getUsers(self):
		params = {}
		url=Url()
		response=self._api.GET(url.users(),params)
		return response

	def getHistory(self):
		params = {}
		url=Url()
		response=self._api.GET(url.panelHistory(),params)
		return response

	def getInfo(self):
		params = {}
		url=Url()
		response=self._api.GET(url.getInfo(),params)
		return response

	def getEnergyHistory(self):
		pass

	def getTemperatureHistory(self):
		pass