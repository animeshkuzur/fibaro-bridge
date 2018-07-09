import sys
from src.api import API
from src.schematic_mapper import Schematic
from src.utils import CSV
import time
# from src.utils import Credentials,Url

class App():
	def __init__(self):
		self.api=API()
		self.schematic=Schematic()
		self.csv=CSV(0)

	def start(self):
		if(self.checkCredentials()):
			print("Authentication complete")
		else:
			print("Incorrect Credentials")
			sys.exit()

		print("Mapping Schematic")

		if(self.schematic.getSchematic()):
			print("Schematic extracted")
		else:
			print("Unable to extract schematic")
			sys.exit()

		print("Extracting Event History")
		if(self.getEventHistory()):
			print("History extracted")
		else:
			print("Unable to extract History")
			sys.exit()

	def checkCredentials(self):
		response=self.api.getLoginStatus()
		if(response['status']):
			return 1
		else:
			return 0

	def getEventHistory(self):
		c=0
		end = int(str(time.time()).split('.')[0])
		start = end-86400
		#response = self.api.getHistory(str(start),str(end))

		csv_row = ['Section ID','Section Name','Room ID','Room Name','Device ID','Device Name','Device Type','Value','DateTime']
		if(self.csv.write(csv_row)):
			pass
		else:
			print("I/O Error Occured")
			sys.exit()
		while(start>0):
			print("Day["+str(c)+"] : Extracting for "+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end)))
			response = self.api.getHistory(str(start),str(end))
			if(self.parser(response)):
				print("Day["+str(c)+"] : Extraction Completed for "+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end)))
			else:
				print("Day["+str(c)+"] : No Data found for "+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end)))
			c=c+1
			end=start
			start=start-86400
			
		print("Done")
		return 1
		#response=self.api.getHistory(start,end)

	def parser(self,data):
		csv_row = []
		roomid=self.schematic.getRoomId(data['deviceID'])
		roomname=self.schematic.getRoomName(roomid)
		sectionid=self.schematic.getSectionId(roomid)
		sectionname=self.schematic.getSectionName(sectionid)
		devicetype=self.schematic.getDeviceTypes(data['deviceID'])
		value=data['value']
		datetime=data['timestamp']
		
		return 1

