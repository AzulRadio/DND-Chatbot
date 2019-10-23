import random

dragon_dict = {'name':'dragon','ID':30334,
               'Str':(3,6,0), 'Dex':(3,6,0), 'Con':(3,6,0), 'Int':(3,6,0), 'Wis':(3,6,0), 'Cha':(3,6,0), 'Health':(5,8,0),'attack1':(2,1,4,2)}      # A dictionary that includes all attributes of dragon
                                                                                                                                # The tuples corresponding to each key refer to the roll_dice parameters (num, sides, adjust)
goblin_dict = {'name':'goblin','ID':34589,
               'Str':(3,6,0), 'Dex':(3,6,0), 'Con':(3,6,0), 'Int':(3,6,0), 'Wis':(3,6,0), 'Cha':(3,6,0), 'Health':(0,0,15)}

human_dict = {'name':'dragon','ID':10001,
               'Str':(3,6,0), 'Dex':(3,6,0), 'Con':(3,6,0), 'Int':(3,6,0), 'Wis':(3,6,0), 'Cha':(3,6,0), 'Health':(5,8,0), 'attack1':(2,1,4,2)}

Monster_dict = {30334: dragon_dict,
                34589: goblin_dict,
                10001: human_dict}    # The one-full-dictionary containing all attributes of all monsters
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
    def __init__(self, abiliscore_dict, name, ID=0, Str=0, Dex=0 , Con=0, Int=0, Wis=0, Cha=0, Health=0):
        self.name = name
        self.ID = abiliscore_dict ['ID']
        self.Str = calc_score_modifier( roll_dice( abiliscore_dict['Str'] ) )
        self.Dex = calc_score_modifier( roll_dice( abiliscore_dict['Dex'] ) )
        self.Con = calc_score_modifier( roll_dice( abiliscore_dict['Con'] ) )
        self.Int = calc_score_modifier( roll_dice( abiliscore_dict['Int'] ) )
        self.Wis = calc_score_modifier( roll_dice( abiliscore_dict['Wis'] ) )
        self.Cha = calc_score_modifier( roll_dice( abiliscore_dict['Cha'] ) )
        self.Health = roll_dice(abiliscore_dict['Health'])
        self.live = 1
    def display_to_dm(self):
        print ("ID = ",self.ID ,"\nname = ",self.name,
               "\nStr = ",self.Str,"\nDex = ",self.Dex,
               "\nCon = ",self.Con,"\nInt = ",self.Int,
               "\nWis = ",self.Wis,"\nCha = ",self.Cha,
               "\nHealth = ",self.Health,"\n")
    def display_to_player(self):
        print("name = %s\n"%(self.name))
    def heal_or_damage(self, heal_or_damage):
        heal_or_damage = heal_or_damage//1
        self.Health = self.Health + heal_or_damage
        if(self.Health <= 0):
            self.live = 0
        else:
            self.live = 1
        self.show_health()
    def show_health(self):
        print("%s, Health = %d\n" %(self.name, self.Health))

    def check_adv_dis(self, state):
        if (state == "adv"):
            check1 = random.randint(1,20)
            check2 = random.randint(1,20)
            check = max(check1, check2)
            print("Adv in checking : %d, %d. result : %d"%(check1,check2,check))
        elif (state == "dis"):
            check1 = random.randint(1,20)
            check2 = random.randint(1,20)
            check = min(check1, check2)
            print("Disadv in checking : %d, %d. result : %d"%(check1,check2,check))
        else:
            check = random.randint(1,20)
        return check

    def check(self, abili, state = 0):
        check = self.check_adv_dis(state)
        if(check == 20):
            print("Check {0} {1} = Natural 20\n".format(self.name, abili))
        elif(check == 1):
            print("Check {0} {1} = Natural l\n".format(self.name, abili))
        else:
            if(type(abili) == type(1)):
                if(abili >=0):
                    print("Check {0} {1} = {2} + {3} = {4}\n".format(self.name, abili, check, abili, check+abili))
                else:
                    print("Check {0} {1} = {2} - {3} = {4}\n".format(self.name, abili, check, abili, check+abili))
                return
            if(getattr(self, abili) >= 0):
                print("Check {0} {1} = {2} + {3} = {4}\n".format(self.name, abili, check, getattr(self, abili), check+getattr(self, abili)))
            else:
                print("Check {0} {1} = {2} - {3} = {4}\n".format(self.name, abili, check, getattr(self, abili)*(-1), check+getattr(self, abili)))
                return
                            #all these if-else make print look nice
            
    def attack(self, state = 0):
        if(self.live == 0):
            return
        abiliscore_dict = Monster_dict[self.ID]
        i = 1
        while('attack'+str(i) in abiliscore_dict):
            damage = 0
            hit_bonus, dice_num, dice_surfaces, fixed_damage = abiliscore_dict['attack'+str(i)]
            i+=1
            attack_check = self.check_adv_dis(state)
            if(attack_check == 20):
                print("Attack check by {0} on {1} = Natural 20\n".format(self.name, ""))
                damage = dice_num * dice_surfaces + fixed_damage
                print("damage = %d\n"%(damage))
            elif(attack_check == 1):
                print("Attack check by {0} on {1} = Natural l\n".format(self.name, ""))
                damage = 0
                print("damage = 0")
            else:
                print("Attack check by {0} on {1} = {2}".format(self.name, "", attack_check))
                damage = roll_dice((dice_num, dice_surfaces, fixed_damage))
                print("damage = %d\n"%(damage))
                        #Now the damage produced by this function can't be taken by another object
                #Todo: use heal_or_damage() to put damage on another object
                
    def designate_target(self, target_total , target_designated = 0):
        if(target_designated > 0):
            print("Designate target %d\n"%(target_designated))
            target = target_designated
        else:
            target = random.randint(1,target_total)
            print("Designate target %d\n"%(target))
        return target
            
            
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

    

def calc_score_modifier(abili_score):
    return (abili_score-10)//2


#Func name:Spawn_Multi_Monsters
#Parameter: unique ID and number of monsters
#Precondition: get attri_dict from Monster_dict
#Postcondition: designated number of members of Class Monster will be spawn and Display To DM will be called
def Spawn_Multi_Monsters(ID, num):
    abiliscore_dict = Monster_dict[ID]
    for i in range(num):
        name = abiliscore_dict['name']+str(i+1)
        globals()[name] = Monster(abiliscore_dict, name)
##        globals()[name].display_to_dm()

#************* test code below ****************#

Spawn_Multi_Monsters(30334,3)
##Spawn_Multi_Monsters(34589,2)
dragon1.show_health()
dragon1.heal_or_damage(-3)
dragon2.display_to_player()
dragon1.check('Con', 'dis')
dragon1.check('Str', 'adv')
dragon1.live = 0
print(dragon1.live)
dragon2.attack()


