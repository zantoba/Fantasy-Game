class ItemClass:
	def __init__(self, ItemName = "Unknown", ItemType='Unknown', ItemDam=0, ItemCost=0):
		self.iName = ItemName
		self.iType = ItemType
		self.iDam = ItemDam
		self.iCost = ItemCost
		
	def ChangeStats(self, Cost, Dam, Type, Name):
		self.iName = Name
		self.iType = Type
		self.iDam = Dam
		self.iCost = Cost
	
	def TestStuff(self):
		print self.iName