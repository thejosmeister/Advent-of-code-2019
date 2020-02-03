# Day 14 pt2

# Open file and remove \n stuff
with open("day14Input.txt") as f:
    list_of_recepies = f.readlines()

list_of_recepies = [x.strip() for x in list_of_recepies]

dict_of_amounts = {}
total_ore = 0
made_temp = 0


# create a tree of these
class Ingredient:
    
    def __init__(self, primary: str, no_produced: int, list_of_ingreds, list_of_numbers):
        self.primary = primary
        self.no_produced = no_produced
        self.list_of_ingreds = list_of_ingreds
        self.list_of_numbers = list_of_numbers


def create_ingredient(input_string: str) -> Ingredient:
    global dict_of_amounts
    ingred_name = pull_out_word(input_string)
    
    dict_of_amounts[ingred_name] = 0
    #find num created
    num = 0
    for recepie in list_of_recepies:
        if recepie[-len(ingred_name):] == ingred_name:
            num = pull_out_number(recepie.split(">")[1])
            
    return Ingredient(pull_out_word(input_string), num, find_children_create_ingreds(ingred_name), find_children_numbers(ingred_name))

def find_children_numbers(ingredient_name: str) -> list:
    output = []
    if ingredient_name == "ORE":
        return output
    for recepie in list_of_recepies:
        if recepie[-len(ingredient_name):] == ingredient_name:
            component = recepie.split("=")[0]
            split_recepie = component.split(",")
            for part in split_recepie:
                output.append(pull_out_number(part))
                
    return output
                
def pull_out_number(input_string: str) -> int:
    output = ""
    for letter in input_string:
        if letter.isnumeric():
            output = output + letter
    
    return int(output)
    
def pull_out_word(input_string: str) -> int:
    output = ""
    for letter in input_string:
        if letter.isalpha():
            output = output + letter
    
    return output
    
def find_children_create_ingreds(ingredient_name: str) -> list:
    output = []
    if ingredient_name == "ORE":
        return output
    for recepie in list_of_recepies:
        if recepie[-len(ingredient_name):] == ingredient_name:
            component = recepie.split("=")[0]
            split_recepie = component.split(",")
            for part in split_recepie:
                output.append(create_ingredient(part))
    
    return output
    

fuel_ingred = create_ingredient("1 FUEL")

# checking i am getting the right stuff
# for ele in fuel_ingred.list_of_ingreds:
    # print (ele.primary)
# for ele in fuel_ingred.list_of_ingreds:
    # print (ele.no_produced)
# for ele in fuel_ingred.list_of_ingreds:
    # print (ele.list_of_numbers)
# print(fuel_ingred.list_of_numbers)
# print(fuel_ingred.no_produced)




def make_ingredient(ingred: Ingredient) -> int:
    global dict_of_amounts
    global total_ore
    made_temp = 0
    
    #print("making: " + ingred.primary)
    #print(dict_of_amounts)
     
    for i in range(len(ingred.list_of_ingreds)):
        #print("state: " + str(i))
        if ingred.list_of_ingreds[i].primary == "ORE":
            total_ore = total_ore + ingred.list_of_numbers[i]
            return ingred.no_produced
        else:
            #print("name " + str(ingred.list_of_ingreds[i].primary) + ", number req: " + str(ingred.list_of_numbers[i]))
            made_temp = 0
            while made_temp + dict_of_amounts[ingred.list_of_ingreds[i].primary] < ingred.list_of_numbers[i]:
                made_temp = made_temp + make_ingredient(ingred.list_of_ingreds[i])
            
            
            dict_of_amounts[ingred.list_of_ingreds[i].primary] = dict_of_amounts[ingred.list_of_ingreds[i].primary] + made_temp - ingred.list_of_numbers[i]
    
    return ingred.no_produced
            


thingy = True
i = 0
fuel_made = 0
previous_state = 0

set_of_remainders = set()
list_of_remainders = []
list_of_total_ores = []
list_of_fuel_made = []


def find_in_list(dict_of_amounts: str) -> int:
    for idd in range(len(list_of_remainders)):
        if list_of_remainders[i] == dict_of_amounts:
            return idd
    return -1


while thingy:
    fuel_made = fuel_made + make_ingredient(fuel_ingred)
    str_of_dict = str(dict_of_amounts)
    if str_of_dict in set_of_remainders:
        previous_state = find_in_list(str_of_dict)
        print("fuel made now = " + str(fuel_made))
        print("fuel madew before = " + str(list_of_fuel_made[previous_state]))
        print("total ore now = " + str(total_ore))
        print("total or before = " + str(list_of_total_ores[previous_state]))
        thingy = False
    else:
        print(fuel_made)
        print("total ore " + str(total_ore))
        set_of_remainders.add(str_of_dict)
        list_of_remainders.append(str_of_dict)
        list_of_total_ores.append(total_ore)
        list_of_fuel_made.append(fuel_made)
        if i > 0:
            print(total_ore - list_of_total_ores[i - 1])
        i = i + 1





print(make_ingredient(fuel_ingred))

print(total_ore)    














