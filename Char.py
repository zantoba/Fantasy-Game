class CharClass:
	""" Character Base Class """
	def SetForce(self):
		self.cForce['health'] = self.cStats['end'] * 3
		self.cForce['mana'] = self.cStats['int'] * 4
		self.cForce['dam'] = self.cStats['str'] * 2
	
	def __init__(self, Name = "NONE", Race = "Human", Class = "Warrior", Stats = {'str': 1, 'int': 1, 'end': 1}):
		self.cName = Name
		self.cRace = Race
		self.cClass = Class
		self.cStats = Stats
		self.cForce = {'health': 1, 'mana': 1, 'dam': 1}
		self.SetForce()
		
	def ChangeStats(self,str,int,end):
		self.cStats['str'] = str
		self.cStats['int'] = int
		self.cStats['end'] = end
		self.SetForce()
		
	def TestStuff(self, Stuff):
		print Stuff
	