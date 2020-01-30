# Should probably have just incorporated standalone intcode machine but I made some modifications to make it work with robot program
#
#

input_string = "3,8,1005,8,311,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,28,1006,0,2,2,109,10,10,1,1,19,10,1,1103,20,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,65,1006,0,33,1,7,0,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,94,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,116,1,1002,1,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,142,2,1101,6,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1001,8,0,168,2,1107,7,10,1006,0,68,1,5,6,10,1,2,5,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,206,1,1008,16,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,232,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,253,1006,0,30,2,1,4,10,1,1008,1,10,2,1109,4,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,291,101,1,9,9,1007,9,1051,10,1005,10,15,99,109,633,104,0,104,1,21102,387508339604,1,1,21102,1,328,0,1106,0,432,21101,0,47677022988,1,21101,0,339,0,1106,0,432,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,209382822080,1,1,21102,386,1,0,1105,1,432,21101,179318123523,0,1,21102,1,397,0,1105,1,432,3,10,104,0,104,0,3,10,104,0,104,0,21102,709584904960,1,1,21101,420,0,0,1106,0,432,21102,709580444008,1,1,21102,431,1,0,1105,1,432,99,109,2,21202,-1,1,1,21102,1,40,2,21101,0,463,3,21101,0,453,0,1105,1,496,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,458,459,474,4,0,1001,458,1,458,108,4,458,10,1006,10,490,1101,0,0,458,109,-2,2106,0,0,0,109,4,2102,1,-1,495,1207,-3,0,10,1006,10,513,21102,1,0,-3,21202,-3,1,1,22102,1,-2,2,21102,1,1,3,21102,532,1,0,1106,0,537,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,560,2207,-4,-2,10,1006,10,560,21201,-4,0,-4,1106,0,628,22101,0,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,579,0,0,1105,1,537,21201,1,0,-4,21101,1,0,-1,2207,-4,-2,10,1006,10,598,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,620,21201,-1,0,1,21101,0,620,0,106,0,495,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0"
array_of_ints = input_string.split(',')
code_map = {}

for i in range(len(array_of_ints)):
    code_map[str(i)] = int(array_of_ints[i])


machine_state = 0
relative_base = 0
halt = False
input_var = 1
input_used = False
output1 = None
output2 = None
robot_action = False
robot_state = [0, 0]
robot_direction = "up"
white_coords = set()
white_coords.add('0,0')
list_of_robot_coords = set()


def set_input(_input: int):
    global input_var
    global input_used
    input_var = _input
    input_used = False


def get_from_map(_machine_state: int):
    interim = code_map.get(str(_machine_state))
    if interim is None:
        interim = 0
    return interim


def get_instruction_code():
    return str(get_from_map(machine_state))[-1]


def process_instruction(_instruction_code: int):
    global halt
    instruction = str(get_from_map(machine_state))

    # print("instruction: " + instruction)
    # print(" ")

    if instruction == "99":
        halt = True
    else:
        length_of_instruction = len(instruction)
        dict_of_modes = determine_param_modes(instruction, length_of_instruction)
        params_for_calc = fetch_inputs(dict_of_modes, _instruction_code)

        if _instruction_code == 1:
            process_1(params_for_calc)
        if _instruction_code == 2:
            process_2(params_for_calc)
        if _instruction_code == 3:
            process_3(params_for_calc)
        if _instruction_code == 4:
            process_4(params_for_calc)
        if _instruction_code == 5:
            process_5(params_for_calc)
        if _instruction_code == 6:
            process_6(params_for_calc)
        if _instruction_code == 7:
            process_7(params_for_calc)
        if _instruction_code == 8:
            process_8(params_for_calc)
        if _instruction_code == 9:
            process_9(params_for_calc)


def determine_param_modes(instruction: str, instruction_length: int) -> dict:
    if instruction_length == 1:
        return {"1": "NORMAL", "2": "NORMAL", "3": "NORMAL"}

    if instruction_length == 3:
        if instruction[0] == "1":
            return {"1": "IMMEDIATE", "2": "NORMAL", "3": "NORMAL"}
        if instruction[0] == "2":
            return {"1": "RELATIVE", "2": "NORMAL", "3": "NORMAL"}

    if instruction_length == 4:
        if instruction[0] == "1":
            if instruction[1] == "1":
                return {"1": "IMMEDIATE", "2": "IMMEDIATE", "3": "NORMAL"}
            if instruction[1] == "2":
                return {"1": "RELATIVE", "2": "IMMEDIATE", "3": "NORMAL"}
            if instruction[1] == "0":
                return {"1": "NORMAL", "2": "IMMEDIATE", "3": "NORMAL"}
        if instruction[0] == "2":
            if instruction[1] == "1":
                return {"1": "IMMEDIATE", "2": "RELATIVE", "3": "NORMAL"}
            if instruction[1] == "2":
                return {"1": "RELATIVE", "2": "RELATIVE", "3": "NORMAL"}
            if instruction[1] == "0":
                return {"1": "NORMAL", "2": "RELATIVE", "3": "NORMAL"}

    if instruction_length == 5:
        if instruction[1] == "1":
            if instruction[2] == "1":
                return {"1": "IMMEDIATE", "2": "IMMEDIATE", "3": "RELATIVE"}
            if instruction[2] == "2":
                return {"1": "RELATIVE", "2": "IMMEDIATE", "3": "RELATIVE"}
            if instruction[2] == "0":
                return {"1": "NORMAL", "2": "IMMEDIATE", "3": "RELATIVE"}
        if instruction[1] == "2":
            if instruction[2] == "1":
                return {"1": "IMMEDIATE", "2": "RELATIVE", "3": "RELATIVE"}
            if instruction[2] == "2":
                return {"1": "RELATIVE", "2": "RELATIVE", "3": "RELATIVE"}
            if instruction[2] == "0":
                return {"1": "NORMAL", "2": "RELATIVE", "3": "RELATIVE"}
        if instruction[1] == "0":
            if instruction[2] == "1":
                return {"1": "IMMEDIATE", "2": "NORMAL", "3": "RELATIVE"}
            if instruction[2] == "2":
                return {"1": "RELATIVE", "2": "NORMAL", "3": "RELATIVE"}
            if instruction[2] == "0":
                return {"1": "NORMAL", "2": "NORMAL", "3": "RELATIVE"}


def fetch_inputs(dict_of_modes: dict, _instruction_code: int) -> dict:
    if _instruction_code == 3:
        return {"param1": fetch_output_param(dict_of_modes["1"], machine_state + 1), "param2": input_var}
    if _instruction_code == 4 or _instruction_code == 9:
        return {"param1": fetch_param(dict_of_modes["1"], machine_state + 1)}
    if _instruction_code == 5 or _instruction_code == 6:
        return {"param1": fetch_param(dict_of_modes["1"], machine_state + 1), "param2": fetch_param(dict_of_modes["2"], machine_state + 2)}

    if _instruction_code == 1 or _instruction_code == 2 or _instruction_code == 7 or _instruction_code == 8:
        return {"param1": fetch_param(dict_of_modes["1"], machine_state + 1), "param2": fetch_param(dict_of_modes["2"], machine_state + 2), "param3": fetch_output_param(dict_of_modes["3"], machine_state + 3)}


def fetch_param(mode: str, place: int) -> int:
    if mode == "NORMAL":
        return get_from_map(get_from_map(place))
    if mode == "IMMEDIATE":
        return get_from_map(place)
    if mode == "RELATIVE":
        return get_from_map(get_from_map(place) + relative_base)


def fetch_output_param(mode: str, place: int) -> int:
    if mode == "NORMAL":
        return get_from_map(place)
    if mode == "RELATIVE":
        return get_from_map(place) + relative_base


# operation 1 processor
def process_1(params_for_calc: dict):
    global machine_state
    code_map[str(params_for_calc["param3"])] = params_for_calc["param1"] + params_for_calc["param2"]
    machine_state = machine_state + 4


def process_2(params_for_calc: dict):
    global machine_state
    code_map[str(params_for_calc["param3"])] = params_for_calc["param1"] * params_for_calc["param2"]
    machine_state = machine_state + 4


def process_3(params_for_calc: dict):
    global machine_state
    global input_used
    code_map[str(params_for_calc["param1"])] = params_for_calc["param2"]
    input_used = True
    machine_state = machine_state + 2


def process_4(params_for_calc: dict):
    global machine_state
    global output1
    global output2
    global robot_action
    if output1 is None:
        output1 = params_for_calc["param1"]
        print("output1: " + str(output1))
    else:
        output2 = params_for_calc["param1"]
        print("output2: " + str(output2))
        robot_action = True


    # bespoke functionality
    # ######
    machine_state = machine_state + 2


def process_5(params_for_calc: dict):
    global machine_state
    if params_for_calc["param1"] == 0:
        machine_state = machine_state + 3
    else:
        machine_state = params_for_calc["param2"]


def process_6(params_for_calc: dict):
    global machine_state
    if params_for_calc["param1"] != 0:
        machine_state = machine_state + 3
    else:
        machine_state = params_for_calc["param2"]


def process_7(params_for_calc: dict):
    global machine_state
    if params_for_calc["param1"] < params_for_calc["param2"]:
        code_map[str(params_for_calc["param3"])] = 1
    else:
        code_map[str(params_for_calc["param3"])] = 0
    machine_state = machine_state + 4


def process_8(params_for_calc: dict):
    global machine_state
    if params_for_calc["param1"] == params_for_calc["param2"]:
        code_map[str(params_for_calc["param3"])] = 1
    else:
        code_map[str(params_for_calc["param3"])] = 0
    machine_state = machine_state + 4


def process_9(params_for_calc: dict):
    global machine_state
    global relative_base
    relative_base = relative_base + params_for_calc["param1"]
    machine_state = machine_state + 2

# # work out parameter settings
# # put values in
# .
# .
# .
# .
# operation 9 processor


def robot_turn_left(_robot_state: list, _robot_direction: str):
    global robot_state
    global robot_direction
    if _robot_direction == "up":
        robot_state[0] = _robot_state[0] - 1
        robot_direction = "left"

    elif _robot_direction == "left":
        robot_state[1] = _robot_state[1] - 1
        robot_direction = "down"

    elif _robot_direction == "down":
        robot_state[0] = _robot_state[0] + 1
        robot_direction = "right"

    elif _robot_direction == "right":
        robot_state[1] = _robot_state[1] + 1
        robot_direction = "up"


def robot_turn_right(_robot_state: list, _robot_direction: str):
    global robot_state
    global robot_direction
    if _robot_direction == "up":
        robot_state[0] = _robot_state[0] + 1
        robot_direction = "right"

    elif _robot_direction == "left":
        robot_state[1] = _robot_state[1] + 1
        robot_direction = "up"

    elif _robot_direction == "down":
        robot_state[0] = _robot_state[0] - 1
        robot_direction = "left"

    elif _robot_direction == "right":
        robot_state[1] = _robot_state[1] - 1
        robot_direction = "down"
# main intcode program


while not halt:
    while not halt and not robot_action:
        # print("machine state: " + str(machine_state))
        # print("relative base: " + str(relative_base))
        # print(code_map)
        instruction_code = get_instruction_code()
        process_instruction(int(instruction_code))

    if not halt:
        print("state of robot: " + str(robot_state[0]) + "," + str(robot_state[1]))
        print("robot direction: " + robot_direction)
        list_of_robot_coords.add(str(robot_state[0]) + "," + str(robot_state[1]))

        if output1 == 1:
            white_coords.add(str(robot_state[0]) + "," + str(robot_state[1]))
        elif str(robot_state[0]) + "," + str(robot_state[1]) in white_coords:
            white_coords.remove(str(robot_state[0]) + "," + str(robot_state[1]))
        output1 = None

        if output2 == 0:
            robot_turn_left(robot_state, robot_direction)
        else:
            robot_turn_right(robot_state, robot_direction)

        output2 = None

        if str(robot_state[0]) + "," + str(robot_state[1]) in white_coords:
            set_input(1)
        else:
            set_input(0)

        print("state of robot: " + str(robot_state[0]) + "," + str(robot_state[1]))

        robot_action = False


print(white_coords)
print(list_of_robot_coords)
print(sorted(list_of_robot_coords))
print(len(list_of_robot_coords))

for j in reversed(range(-100, 100)):
    for i in range(-100, 100):
        if i == -99:
            if str(i) + "," + str(j) in white_coords:
                print("#")
            else:
                print(".")
        else:
            if str(i) + "," + str(j) in white_coords:
                print("#", end = "")
            else:
                print(".", end = "")
