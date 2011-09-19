import Char
import random
import Item

class NPCClass(Char.CharClass):
	LootTable = []
	addItem = Item.ItemClass
	def SetLoot(self):
		self.LootTable.append(self.addItem)
	
	def GetLoot(self):
		if len(self.LootTable) > 0:
			LootItem = self.LootTable[random.randint(0, (len(self.LootTable))-1)]
			return LootItem
		else:
			return self.addItem
			
	def TestStuff(self, Stuff):
		print Stuff
	