import requests
from src.utils import base64

class API_Request():
	def __init__(self,url,params):
		self._url=url
		self._params=params
		self._headers={"Authorization":"Basic ".key}

	def POST(self):
		try:
			response = requests.post(url=self._url,params=self._params,headers=self._headers)
		except requests.exceptions.ConnectionError:
			print("Connection refused")
			return -1
		data = response.json()
		return data

	def GET():
		pass

	def PUT():
		pass

	def DELETE():
		pass

	def UPDATE():
		pass