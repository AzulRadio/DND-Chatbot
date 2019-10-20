import random
class Monster:
    def __init__(self, ID, Str, Dex, Con, Int, Wis, Cha, Health):
##    def __init__(self, ID, Str):
        self.ID = ID
        self.Str = Str
        self.Dex = Dex
        self.Con = Con
        self.Int = Int
        self.Wis = Wis
        self.Cha = Cha
        self.Health = Health
    def Display_To_DM(self):
        print ("ID = ",self.ID ,"\nStr = ",self.Str,
               "\nDex = ",self.Dex,"\nCon = ",self.Con,
               "\nDex = ",self.Dex ,"\nInt = ",self.Int,
               "\nWis = ",self.Wis,"\nCha = ",self.Cha,
               "\nHealth = ",self.Health)

## Func name: Attribute_Generate()
## Parameter: a member variable of class Monster
## Precondition: input member variable of class Monster
## Postcondition: assign all attributes of this member
def Attribute_Generate(self):
    self.ID = 1
    self.Str = roll_dice(3,6)
    self.Dex = roll_dice(3,6)
    self.Con = roll_dice(3,6)
    self.Int = roll_dice(3,6)
    self.Wis = roll_dice(3,6)
    self.Cha = roll_dice(3,6)
    self.Health = roll_dice(5,8)

##Func name:roll_dice()
##Parameter: number of dice and surface number of the dice
##Precondition:num and surface are positive integer
##Postcondition: return the sum of the dice
def roll_dice(num, surfaces):

    sum = 0
    while (num>0):
        sum = sum + random.randint(1,surfaces)
        num = num -1
    return sum

##This is a failed function, I am trying to spawn multiple monster at the same time.
##def Spawn_Multi_Monsters(num):
##    for i in range(1,3):
##        locals()['mon'+str(i)] = Monster(0,0,0,0,0,0,0,0)
##        Attribute_Generate(locals()['mon'+str(i)])

mon1 = Monster(0,0,0,0,0,0,0,0)
Attribute_Generate(mon1)
##Spawn_Multi_Monsters(3)
mon1.Display_To_DM()
