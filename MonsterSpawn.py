import random
import time




dragon_dict = {'name':'dragon','ID':30334,
               'Str':(3,6), 'Dex':(3,6), 'Con':(3,6), 'Int':(3,6), 'Wis':(3,6), 'Cha':(3,6), 'Health':(5,8)}      # A dictionary that includes all attributes of dragon
                                                                                                                  # The tuples corresponding to each key refer to the roll_dice parameters
goblin_dict = {'name':'goblin','ID':34589,
               'Str':(3,6), 'Dex':(3,6), 'Con':(3,6), 'Int':(3,6), 'Wis':(3,6), 'Cha':(3,6), 'Health':(2,8)}


Monster_dict = {30334: dragon_dict,
                34589: goblin_dict}    # The one-full-dictionary containing all attributes of all monsters
                                      # TO DO: make it a json file

'''
# unfinished
# Parameter: ID unique to each kind of monster
# Precondition: input ID
# Postcondition: return a List from database with name(List[0]) and attributes chance but not numbers, for example, Str = 5d6)
attri_displacement = 1
# in case we have to add more things in the attri_dict between name and attribute
def convert_id_to_attri(ID):
    attri_dict = {'name':'dragon','ID':ID,
                  'Str':(3,6), 'Dex':(3,6), 'Con':(3,6), 'Int':(3,6), 'Wis':(3,6), 'Cha':(3,6), 'Health':(5,8)}#Correspounding order as in Monster Class
    return attri_dict
#unfinished
'''



class Monster:
    def __init__(self, attri_dict, name, ID=0, Str=0, Dex=0 , Con=0, Int=0, Wis=0, Cha=0, Health=0):
#    def __init__(self, ID, Str):
        self.name = name
        self.ID = attri_dict ['ID']
        self.Str = roll_dice(attri_dict['Str'])
        self.Dex = roll_dice(attri_dict['Dex'])
        self.Con = roll_dice(attri_dict['Con'])
        self.Int = roll_dice(attri_dict['Int'])
        self.Wis = roll_dice(attri_dict['Wis'])
        self.Cha = roll_dice(attri_dict['Cha'])
        self.Health = roll_dice(attri_dict['Health'])
    def Display_To_DM(self):
        print ("ID = ",self.ID ,"\nname = ",self.name,
               "\nStr = ",self.Str,"\nDex = ",self.Dex,
               "\nCon = ",self.Con,"\nInt = ",self.Int,
               "\nWis = ",self.Wis,"\nCha = ",self.Cha,
               "\nHealth = ",self.Health,"\n")

#Func name:roll_dice()
#Parameter: tuple with format (num, sides)
#Precondition:num and sides are positive integer
#Postcondition: return the result
def roll_dice(ndx):
    n,x = ndx
    sum = 0
    while (n >0):
        sum += random.randint(1,x)
        n -= 1
    return sum


#Func name:Spawn_Multi_Monsters
#Parameter: unique ID and number of monsters
#Precondition: get attri_dict from Monster_dict
#Postcondition: designated number of members of Class Monster will be spawn and Display To DM will be called
def Spawn_Multi_Monsters(ID, num):
    attri_dict = Monster_dict[ID]
    for i in range(num):
        name = attri_dict['name']+str(i+1)
        globals()[name] = Monster(attri_dict, name)
        globals()[name].Display_To_DM()

#************* test code below ****************#

Spawn_Multi_Monsters(30334,3)
Spawn_Multi_Monsters(34589,2)
#spawn 3 monsters with ID 30334
#check convert_id_to_attri() for more details
#whatever ID you put you can only spawn dragon
