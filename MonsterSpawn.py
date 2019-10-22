import random

dragon_dict = {'name':'dragon','ID':30334,
               'Str':(3,6,0), 'Dex':(3,6,0), 'Con':(3,6,0), 'Int':(3,6,0), 'Wis':(3,6,0), 'Cha':(3,6,0), 'Health':(5,8,0)}      # A dictionary that includes all attributes of dragon
                                                                                                                                # The tuples corresponding to each key refer to the roll_dice parameters (num, sides, adjust)
goblin_dict = {'name':'goblin','ID':34589,
               'Str':(3,6,0), 'Dex':(3,6,0), 'Con':(3,6,0), 'Int':(3,6,0), 'Wis':(3,6,0), 'Cha':(3,6,0), 'Health':(0,0,15)}


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
        self.name = name
        self.ID = attri_dict ['ID']
        self.Str = calc_adjust_value(roll_dice(attri_dict['Str']))
        self.Dex = calc_adjust_value(roll_dice(attri_dict['Dex']))
        self.Con = calc_adjust_value(roll_dice(attri_dict['Con']))
        self.Int = calc_adjust_value(roll_dice(attri_dict['Int']))
        self.Wis = calc_adjust_value(roll_dice(attri_dict['Wis']))
        self.Cha = calc_adjust_value(roll_dice(attri_dict['Cha']))
        self.Health = roll_dice(attri_dict['Health'])
    def display_to_dm(self):
        print ("ID = ",self.ID ,"\nname = ",self.name,
               "\nStr = ",self.Str,"\nDex = ",self.Dex,
               "\nCon = ",self.Con,"\nInt = ",self.Int,
               "\nWis = ",self.Wis,"\nCha = ",self.Cha,
               "\nHealth = ",self.Health,"\n")
    def display_to_player(self):
        print("name = ",self.name)
    def heal_or_damage(self, heal_or_damage):
        heal_or_damage = heal_or_damage//1
        self.Health = self.Health + heal_or_damage
    def show_health(self):
        print("name = ",self.name,"\nHealth = ",self.Health,"\n")


#Func name: roll_dice()
#Parameter: tuple with format (num, sides, adjustment)
#Precondition:num, sides and adjustment are positive integer
#Postcondition: return the result of rolling
def roll_dice(ndxpy):
    n,x,y = ndxpy
    sum = 0
    while (n >0):
        sum += random.randint(1,x)
        n -= 1
    return sum + y

def calc_adjust_value(attri_value):
    return (attri_value-10)//2


#Func name:Spawn_Multi_Monsters
#Parameter: unique ID and number of monsters
#Precondition: get attri_dict from Monster_dict
#Postcondition: designated number of members of Class Monster will be spawn and Display To DM will be called
def Spawn_Multi_Monsters(ID, num):
    attri_dict = Monster_dict[ID]
    for i in range(num):
        name = attri_dict['name']+str(i+1)
        globals()[name] = Monster(attri_dict, name)
        globals()[name].display_to_dm()

#************* test code below ****************#

Spawn_Multi_Monsters(30334,3)
Spawn_Multi_Monsters(34589,2)
dragon1.show_health()
dragon1.heal_or_damage(-3)
dragon1.show_health()
dragon2.show_health()
#spawn 3 monsters with ID 30334
#check convert_id_to_attri() for more details
#whatever ID you put you can only spawn dragon
