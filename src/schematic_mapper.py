import sys
from os.path import abspath, isfile
from src.api import API
from src.utils import CSV

class Schematic():
	def __init__(self):
		self.api=API()
		self.rooms={}
		self.sections={}
		self.devices={}
		self.device_type={}
		self.section_room={}
		self.room_device={}
		self.csv=CSV(1)

	def getSchematic(self):
		if(self.getMetaData()==0):
			sys.exit()
		print("Meta Data Collected")

		self.getSections()
		print(self.sections)

		self.getRooms()
		print(self.rooms)
		print(self.section_room)

		self.getDevices()
		print(self.devices)
		print(self.room_device)
		print(self.device_type)

		print(self.getRoomId(353))
		print(self.rooms[self.getRoomId(353)])

	def getDevices(self):
		response=self.api.getDevices()
		for res in response:
			self.devices[res['id']]=res['name']
			self.room_device[res['roomID']]=res['id']
			self.device_type[res['id']]=res['type']
		return 1

	def getRoomId(self,device):
		for roomID,deviceID in self.room_device.items():
			if(device==deviceID):
				return roomID
			else:
				return -1

	def getRooms(self):
		response=self.api.getRooms()
		for res in response:
			self.rooms[res['id']]=res['name']
			self.section_room[res['sectionID']]=res['id']
		return 1

	def getSections(self):
		response=self.api.getSections()
		for res in response:
			self.sections[res['id']]=res['name']
		return 1

	def getSectionId(self,room):
		pass

	def getDeviceTypes(self,device):
		pass

	def getMetaData(self):
		response=self.api.getInfo()
		self.csv.write(['HC Name','Serial Number','MAC Address'])
		self.csv.write([response['hcName'],response['serialNumber'],response['mac']])
		print("Extracting for : "+response['hcName'])
		return 1


