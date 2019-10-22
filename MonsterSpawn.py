import random
import time
attri_displacement = 1
#in case we have to add more things in the attri_list between name and attribute


#unfinished
#Parameter: ID unique to each kind of monster
#Precondition: input ID
#Postcondition: return a List from database with name(List[0]) and attributes chance but not numbers, for example, Str = 5d6)
def convert_id_to_attri(ID):
    attri_list = ['dragon',ID ,3,6,3,6,3,6,3,6,3,6,3,6,5,8]#Correspounding order as in Monster Class
    return attri_list
#unfinished


class Monster:
    def __init__(self, attri_list, name, ID=0, Str=0, Dex=0 , Con=0, Int=0, Wis=0, Cha=0, Health=0):
#    def __init__(self, ID, Str):
        self.name = name
        self.ID = attri_list [1]
        self.Str = roll_dice(attri_list[attri_displacement + 1],attri_list[attri_displacement + 2])
        self.Dex = roll_dice(attri_list[attri_displacement + 3],attri_list[attri_displacement + 4])
        self.Con = roll_dice(attri_list[attri_displacement + 5],attri_list[attri_displacement + 6])
        self.Int = roll_dice(attri_list[attri_displacement + 7],attri_list[attri_displacement + 8])
        self.Wis = roll_dice(attri_list[attri_displacement + 9],attri_list[attri_displacement + 10])
        self.Cha = roll_dice(attri_list[attri_displacement + 11],attri_list[attri_displacement + 12])
        self.Health = roll_dice(attri_list[attri_displacement + 13],attri_list[attri_displacement + 14])
    def Display_To_DM(self):
        print ("ID = ",self.ID ,"\nname = ",self.name,
               "\nStr = ",self.Str,"\nDex = ",self.Dex,
               "\nCon = ",self.Con,"\nInt = ",self.Int,
               "\nWis = ",self.Wis,"\nCha = ",self.Cha,
               "\nHealth = ",self.Health,"\n")

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
#Func name:Spawn_Multi_Monsters
#Parameter: unique ID and number of monsters
#Precondition: convert_id_to_attri() can return a list with all attributes
#Postcondition: designated number of members of Class Monster will be spawn and Display To DM will be called
def Spawn_Multi_Monsters(ID, num):
    attri_list = convert_id_to_attri(ID)
    for i in range(num):
        globals()[attri_list[0]+str(i+1)] = Monster(attri_list, attri_list[0]+str(i+1))
        globals()[attri_list[0]+str(i+1)].Display_To_DM()

#************* test code below ****************#

Spawn_Multi_Monsters(30334,3)
#spawn 3 monsters with ID 30334
#check convert_id_to_attri() for more details
#whatever ID you put you can only spawn dragon
