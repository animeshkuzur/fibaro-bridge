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
		#print("Meta Data Collected")

		if(self.getSections()!=1):
			print("error occured while mapping sections")
			sys.exit()
		#print(self.sections)

		if(self.getRooms()!=1):
			print("error occured while mapping rooms")
			sys.exit()
		#print(self.rooms)
		#print(self.section_room)

		if(self.getDevices()!=1):
			print("error occured while mapping devices")
			sys.exit()

		#print(self.devices)
		#print(self.room_device)
		#print(self.device_type)
		return 1

	def getDeviceName(self,device):
		return self.devices[device]

	def getDevices(self):
		response=self.api.getDevices()
		for res in response:
			self.devices[res['id']]=res['name']
			self.room_device.setdefault(res['roomID'],[])
			self.room_device[res['roomID']].append(res['id'])
			self.device_type[res['id']]=res['type']
		return 1

	def getRoomName(self,room):
		return self.rooms[room]

	def getRoomId(self,device):
		for roomID,deviceIDs in self.room_device.items():
			for deviceID in deviceIDs:
				if(device==deviceID):
					return roomID
				else:
					flag = 0
		return flag

	def getRooms(self):
		response=self.api.getRooms()
		for res in response:
			self.rooms[res['id']]=res['name']
			self.section_room.setdefault(res['sectionID'],[])
			self.section_room[res['sectionID']].append(res['id'])
		return 1

	def getSections(self):
		response=self.api.getSections()
		for res in response:
			self.sections[res['id']]=res['name']
		return 1

	def getSectionName(self,section):
		return self.sections[section]

	def getSectionId(self,room):
		for sectionID,roomIDs in self.section_room.items():
			for roomID in roomIDs:
				if(room==roomID):
					return sectionID
				else:
					flag = 0
		return flag

	def getDeviceTypes(self,device):
		return self.device_type[device]

	def getMetaData(self):
		response=self.api.getInfo()
		self.csv.write(['HC Name','Serial Number','MAC Address'])
		self.csv.write([response['hcName'],response['serialNumber'],response['mac']])
		print("Extracting for : "+response['hcName'])
		return 1

	def getDeviceValue(self,device,value):
		pass

