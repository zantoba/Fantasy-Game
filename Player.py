import Char
import Item

class PlayerClass(Char.CharClass):
	pBag = []
	addItem = Item.ItemClass
	def AddItem(self, addItem):
		self.pBag.append(addItem)
		
	def AdjustStats(self, pBag):
		pass
	
	def MoveSelf(self, Dir):
		pass
		
	def TestStuff(self, Stuff):
		print Stuff
	