import requests
from src.utils import Credentials
import json

class API_Request():
	def __init__(self):
		x=Credentials()
		key=x.getCredentials()
		self._headers={"Authorization":"Basic "+key}

	def POST(self,url,params):
		try:
			response = requests.post(url=url,params=params,headers=self._headers)
		except requests.exceptions.ConnectionError:
			print("Connection refused")
			return -1
		data = response.json()
		return data

	def GET(self,url,params):
		try:
			response = requests.get(url=url,params=params,headers=self._headers)
		except requests.exceptions.ConnectionError:
			print("Connection refused")
			return -1
		data = response.json()
		return data

	def PUT(self,url,params):
		try:
			response = requests.put(url=url,params=params,headers=self._headers)
		except requests.exceptions.ConnectionError:
			print("Connection refused")
			return -1
		data = response.json()
		return data

	def DELETE(self,url,params):
		try:
			response = requests.delete(url=url,params=params,headers=self._headers)
		except requests.exceptions.ConnectionError:
			print("Connection refused")
			return -1
		data = response.json()
		return data

	def UPDATE(self,url,params):
		try:
			response = requests.update(url=url,params=params,headers=self._headers)
		except requests.exceptions.ConnectionError:
			print("Connection refused")
			return -1
		data = response.json()
		return data