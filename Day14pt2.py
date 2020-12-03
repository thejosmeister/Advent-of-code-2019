# Day 14 pt2

# Did this after about 3 days of thinking. Eventually went with finding the average amount of ore required for 1000 fuel.
# Once you find the average you can find the remaing ore from the trillion and run the make_ingredient alg until it has been used up.
# The initial fuel made will require more ore as there are no remainders of products.
# A sample of 10 iterations produced an average that gave me an answer too high (3849044).
# A smaple of 100 iteratrions was more successful giving me the right answer (3848998).


# The code below is left in the state I used to find the fuel made from the remaining ore.


import time

# Open file and remove \n stuff
with open("Inputs/day14Input.txt") as f:
    list_of_recepies = f.readlines()

list_of_recepies = [x.strip() for x in list_of_recepies]

dict_of_amounts = {}
amount_made = {}
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
    amount_made[ingred_name] = 0
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
    
# Sets up map of ingredients that will be iterated over
fuel_ingred = create_ingredient("1 FUEL")





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
            amount_made[ingred.primary] = amount_made[ingred.primary] + ingred.no_produced
            return ingred.no_produced
        else:
            #print("name " + str(ingred.list_of_ingreds[i].primary) + ", number req: " + str(ingred.list_of_numbers[i]))
            made_temp = 0
            while made_temp + dict_of_amounts[ingred.list_of_ingreds[i].primary] < ingred.list_of_numbers[i]:
                made_temp = made_temp + make_ingredient(ingred.list_of_ingreds[i])
            
            amount_made[ingred.list_of_ingreds[i].primary] = amount_made[ingred.list_of_ingreds[i].primary] + made_temp
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

tic = time.perf_counter()
times = 0

# Make first ingred to populate a set of remainders.
make_ingredient(fuel_ingred)

# Sample of the dictionary containing amounts after producing 1 fuel.
# dict_of_amounts = {'FUEL': 0, 'MHJMX': 6, 'LTHFW': 8, 'SWZCB': 2, 'GDNG': 4, 'LBHQ': 2, 'CXNM': 2, 'ZNPRL': 6, 'ORE': 0, 'PDVR': 5, 'TZMWG': 2, 'QZQLZ': 0, 'VFXHC': 0, 'MJQS': 1, 'HMRGM': 0, 'XPTXL': 4, 'HNCDS': 0, 'SMSB': 0, 'MTQCB': 2, 'FWZN': 1, 'PDCV': 4, 'PFQRG': 1, 'XVNL': 8, 'PBMPL': 1, 'PRXT': 1, 'FDVH': 1, 'THRVR': 3, 'XHPHR': 0, 'GSMP': 2, 'NWNSH': 1, 'JRZXM': 0, 'NSVJL': 4, 'RNMKC': 0, 'MHBZ': 2, 'HJVN': 0, 'WPFP': 1, 'XRDN': 0, 'VPSDV': 1, 'MRVFT': 5, 'NTJZH': 3, 'JMWQG': 6, 'XHQDX': 0, 'ZFCD': 0, 'SVSTJ': 1, 'HJTD': 5, 'LDHX': 3, 'ZBNCP': 2, 'VJTFJ': 1, 'LBQB': 6, 'DLWT': 0, 'ZXMGK': 0, 'JTXWX': 0, 'XSFVQ': 5, 'BNMWF': 3, 'PBNSF': 0, 'MJCLX': 0, 'QWRB': 8, 'SVNVJ': 4, 'JCHP': 0, 'GHVN': 0, 'QZNCK': 1}


# code to find averages commented out:

list_of_total_ores.append(total_ore)
# while times < 100:
#     fuel_made = 0
#     total_ore_start = total_ore
while total_ore < 259681800:
    fuel_made = fuel_made + make_ingredient(fuel_ingred)


    print(fuel_made)
    # list_of_total_ores.append(total_ore - total_ore_start)
    # times = times + 1

toc = time.perf_counter()

print("time taken " + str(toc - tic))



# summ = 0
# for ore in list_of_total_ores[1:]:
#     summ = summ + ore

# print("ans = " + str(summ/len(list_of_total_ores[1:])))
print(total_ore) 

