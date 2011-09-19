import DiceBag
import Char
import Item
import NPC
import Player

class CombatClass:
	enemy = NPC.NPCClass()
	player = Player.PlayerClass()
	def DoBattle(self,player = Player.PlayerClass(),enemy = NPC.NPCClass()):
		while enemy.cForce['health'] > 0 and player.cForce['health'] > 0:
			EnDam = (enemy.cForce['dam'] * DiceBag.D20(1)[0])
			PlayDam = (player.cForce['dam'] * DiceBag.D20(1)[0])
			if  EnDam > PlayDam:
				print "Player takes damage!"
				player.cForce['health'] = player.cForce['health'] - EnDam
			elif PlayDam > EnDam:
				print "Enemy takes damage!"
				enemy.cForce['health'] = enemy.cForce['health'] - PlayDam
			else:
				print "They deflected eachother's attacks!"
				
		if enemy.cForce['health'] > player.cForce['health']:
			print "SON I AM DISSAPOINT!"
			self.GiveLoot(player,enemy)
		elif player.cForce['health'] > enemy.cForce['health']:
			print "ENEMY PWND!"
			self.GiveLoot(player,enemy)
		else:
			print "TOTAL DOOM!"
		
	def GiveLoot(self,player,enemy):
		player.AddItem(enemy.GetLoot())
		