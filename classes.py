#This is the Class Sheet for AQ.
#Base Classes
class Char():
    hp=None
    heals=None
    dmg=None
    ammo=None#For ranged weapon
    eff=None#Like an burn effect

class Player(Char):
    hp=None
    heals=None
    dmg=None
    ammo=None
    eff=None
#Mob Classes
class Slime(Char):#Very weak Mob
    hp=20
    dmg=10
class Goblin(Char):
    hp=70
    heals=1
    dmg=20
    ammo=1
 
 #Player Classes
class Brute(Player):
    hp=150
    dmg=35
class Ranger(Player):
    hp=75
    heals=3
    dmg=10
    ammo=10
class Healer(Player):
    hp=75
    heals=10
    dmg=20

