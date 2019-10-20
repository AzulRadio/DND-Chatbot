import random
import time
class Monster:
    def __init__(self, name, ID=0, Str=0, Dex=0 , Con=0, Int=0, Wis=0, Cha=0, Health=0):
#    def __init__(self, ID, Str):
        self.name = name
        self.ID = ID
        self.Str = Str
        self.Dex = Dex
        self.Con = Con
        self.Int = Int
        self.Wis = Wis
        self.Cha = Cha
        self.Health = Health
    def Display_To_DM(self):
        print ("name = ",self.name,"\nID = ",self.ID ,
               "\nStr = ",self.Str,"\nDex = ",self.Dex,
               "\nCon = ",self.Con,"\nInt = ",self.Int,
               "\nWis = ",self.Wis,"\nCha = ",self.Cha,
               "\nHealth = ",self.Health,"\n")

# Func name: Attribute_Generate()
# Parameter: a member variable of class Monster
# Precondition: input member variable of class Monster
# Postcondition: assign all attributes of this member
def Attribute_Generate(self):
    self.ID = 1
    self.Str = roll_dice(3,6)
    self.Dex = roll_dice(3,6)
    self.Con = roll_dice(3,6)
    self.Int = roll_dice(3,6)
    self.Wis = roll_dice(3,6)
    self.Cha = roll_dice(3,6)
    self.Health = roll_dice(5,8)

#Func name:roll_dice()
#Parameter: number of dice and surface number of the dice
#Precondition:num and surface are positive integer
#Postcondition: return the sum of the dice
def roll_dice(num, surfaces):

    sum = 0
    while (num>0):
        sum += random.randint(1,surfaces)
        num -= 1
    return sum

#This function is fixed by kevinskwk by changing locals() to globals()
def Spawn_Multi_Monsters(name, n):
    for i in range(n):
        globals()[name+str(i+1)] = Monster(name+str(i+1))
        Attribute_Generate(globals()[name+str(i+1)])

goblin = Monster('goblin')
Attribute_Generate(goblin)
goblin.Display_To_DM()

Spawn_Multi_Monsters('dragon',3)
dragon1.Display_To_DM()
dragon2.Display_To_DM()
dragon3.Display_To_DM()
