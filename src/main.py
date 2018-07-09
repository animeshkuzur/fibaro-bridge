import sys
from src.api import API
from src.schematic_mapper import Schematic
from src.utils import CSV
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

	def checkCredentials(self):
		response=self.api.getLoginStatus()
		if(response['status']):
			return 1
		else:
			return 0

	def getEventHistory(self):
		pass


