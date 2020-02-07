
from Day15IntcodeMachineClass import IntcodeMachine

robot_position = [0, 0]
robot_distance_from_centre = 0
robot_stop = False
set_of_walls = set()
set_of_spaces = set()
set_of_spaces.add(str(robot_position))
location_of_oxygen = None
distances_from_centre = {str(robot_position): 0}
input_movement = 0

input_string = "3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,1002,1034,1,1039,1001,1036,0,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1105,1,124,1001,1034,0,1039,102,1,1036,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1105,1,124,1001,1034,-1,1039,1008,1036,0,1041,101,0,1035,1040,102,1,1038,1043,1001,1037,0,1042,1106,0,124,1001,1034,1,1039,1008,1036,0,1041,1001,1035,0,1040,102,1,1038,1043,1001,1037,0,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,9,1032,1006,1032,165,1008,1040,5,1032,1006,1032,165,1101,0,2,1044,1105,1,224,2,1041,1043,1032,1006,1032,179,1102,1,1,1044,1106,0,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,40,1044,1106,0,224,1101,0,0,1044,1106,0,224,1006,1044,247,102,1,1039,1034,101,0,1040,1035,101,0,1041,1036,1001,1043,0,1038,1001,1042,0,1037,4,1044,1106,0,0,26,29,83,66,1,36,14,44,33,12,3,15,20,56,9,35,51,55,6,20,13,71,15,23,94,38,45,15,47,30,89,39,11,55,5,9,47,29,41,36,78,12,4,65,48,66,36,94,76,30,63,41,32,1,73,1,35,65,87,46,18,90,11,44,30,73,87,8,38,46,17,78,51,34,19,53,37,26,20,24,46,64,17,6,26,41,10,62,14,88,23,94,13,55,5,45,10,39,83,99,32,34,72,30,58,33,71,47,21,38,97,38,46,41,18,39,37,8,86,55,35,4,92,19,21,53,61,6,55,69,16,85,62,26,63,17,80,33,10,53,91,2,37,94,37,93,7,97,18,55,54,36,17,62,89,12,92,32,69,4,46,47,19,89,25,12,51,91,9,1,71,35,56,39,98,48,7,49,24,95,15,45,2,1,93,82,19,7,11,70,30,64,28,27,58,4,39,30,94,72,33,43,90,98,26,32,70,1,81,25,35,47,17,31,92,15,73,13,27,72,65,30,67,2,22,89,77,30,47,12,58,26,79,22,37,74,41,3,42,30,39,67,24,18,62,98,19,59,95,25,6,67,42,35,85,51,48,7,63,17,67,53,45,13,25,43,1,54,4,65,55,20,73,32,70,1,33,39,93,88,19,35,56,21,13,53,73,31,21,44,73,31,13,69,30,42,26,51,25,90,16,49,9,93,50,28,60,24,18,61,23,11,98,19,45,77,12,61,31,3,66,56,4,77,24,59,87,31,38,65,67,7,9,23,71,9,59,35,55,83,22,12,94,17,67,87,96,63,8,29,32,34,15,55,39,60,41,74,39,81,47,51,25,26,57,28,18,60,84,20,16,66,42,14,25,16,94,2,22,74,85,19,63,32,9,19,11,91,44,34,21,1,56,12,87,8,52,18,56,7,90,5,86,81,24,98,21,9,80,59,68,10,80,53,18,75,50,9,14,43,26,29,57,86,39,41,93,3,69,55,16,84,15,22,84,30,72,19,13,15,19,80,97,79,32,68,77,82,30,19,4,71,45,67,14,95,17,54,80,88,25,13,80,41,37,96,15,28,26,33,73,32,45,79,21,52,23,98,82,21,16,13,64,32,39,93,17,33,95,61,36,12,21,3,84,4,88,22,26,59,80,27,82,2,85,79,29,33,52,17,23,95,8,64,16,56,23,42,43,18,41,11,9,84,42,62,4,67,17,98,76,99,1,16,72,72,10,79,19,76,4,54,9,99,34,33,7,97,85,19,76,93,38,6,90,37,90,2,83,61,19,43,39,2,91,17,60,21,79,2,32,94,38,32,7,64,8,14,7,68,23,28,75,24,73,50,29,63,22,89,4,51,66,2,7,33,82,13,23,84,81,23,55,68,15,27,9,97,27,79,42,86,75,56,13,95,74,5,88,25,44,99,33,14,24,29,21,78,4,15,75,32,92,74,11,56,24,57,10,28,73,8,10,90,77,30,96,8,60,3,71,20,41,9,33,89,38,74,95,4,95,35,13,18,55,10,81,9,60,17,67,7,34,48,48,15,54,79,37,66,43,22,64,28,28,4,91,5,9,92,30,64,37,98,66,15,92,2,3,25,70,25,33,61,56,25,70,58,30,41,97,18,54,10,49,45,3,1,30,57,30,46,8,55,79,39,58,46,35,19,38,80,86,4,36,75,29,62,39,71,2,41,6,66,36,99,21,61,39,72,3,48,29,43,31,59,84,71,12,52,61,82,11,56,23,51,30,60,88,65,35,48,24,58,76,49,93,51,33,72,0,0,21,21,1,10,1,0,0,0,0,0,0"

machine = IntcodeMachine(input_string)


def find_observed_square() -> list:
    global robot_position
    global input_movement
    if input_movement == 1:
        return [robot_position[0], robot_position[1] + 1]
    if input_movement == 2:
        return [robot_position[0], robot_position[1] - 1]
    if input_movement == 3:
        return [robot_position[0] - 1, robot_position[1]]
    if input_movement == 4:
        return [robot_position[0] + 1, robot_position[1]]


def process_output(output: int):
    global robot_position
    global location_of_oxygen
    global set_of_walls
    global set_of_spaces
    global robot_distance_from_centre
    global distances_from_centre
    if output == -1:
        return
    observed_square = find_observed_square()
    print("observed" + str(observed_square))
    if output == 0:
        set_of_walls.add(str(observed_square))
        return
    if output == 1:

        robot_position = observed_square
        if is_square_discovered(observed_square):
            robot_distance_from_centre = distances_from_centre[str(observed_square)]
        else:
            set_of_spaces.add(str(observed_square))
            robot_distance_from_centre = robot_distance_from_centre + 1
            distances_from_centre[str(observed_square)] = robot_distance_from_centre
        return
    if output == 2:

        robot_position = observed_square
        if is_square_discovered(observed_square):
            robot_distance_from_centre = distances_from_centre[str(observed_square)]
        else:
            location_of_oxygen = str(observed_square)
            robot_distance_from_centre = robot_distance_from_centre + 1
            distances_from_centre[str(observed_square)] = robot_distance_from_centre
        return


def is_square_discovered(square: list) -> bool:
    global set_of_spaces
    global set_of_walls
    global location_of_oxygen
    if str(square) in set_of_walls or str(square) in set_of_spaces or str(location_of_oxygen) == str(square):
        return True
    else:
        return False


def check_robot_finished():
    global robot_position
    global robot_stop
    if robot_position == [0, 0]:
        if is_square_discovered([0, 1]) and is_square_discovered([0, -1]) and is_square_discovered([1, 0]) and is_square_discovered([-1, 0]):
            robot_stop = True


def move_robot_to_shortest_dist(robot_pos: list) -> int:
    global robot_distance_from_centre
    global distances_from_centre
    global set_of_walls
    output = 0
    current_smallest = robot_distance_from_centre
    if not str([robot_pos[0], robot_pos[1] + 1]) in set_of_walls:
        if distances_from_centre[str([robot_pos[0], robot_pos[1] + 1])] < current_smallest:
            output = 1

    if not str([robot_pos[0], robot_pos[1] - 1]) in set_of_walls:
        if distances_from_centre[str([robot_pos[0], robot_pos[1] - 1])] < current_smallest:
            output = 2

    if not str([robot_pos[0] + 1, robot_pos[1]]) in set_of_walls:
        if distances_from_centre[str([robot_pos[0] + 1, robot_pos[1]])] < current_smallest:
            output = 4

    if not str([robot_pos[0] - 1, robot_pos[1]]) in set_of_walls:
        if distances_from_centre[str([robot_pos[0] - 1, robot_pos[1]])] < current_smallest:
            output = 3

    return output


def determine_input():
    global robot_position
    global input_movement
    print("robot position" + str(robot_position))
    if not is_square_discovered([robot_position[0], robot_position[1] + 1]):
        input_movement = 1
        return
    if not is_square_discovered([robot_position[0], robot_position[1] - 1]):
        input_movement = 2
        return
    if not is_square_discovered([robot_position[0] - 1, robot_position[1]]):
        input_movement = 3
        return
    if not is_square_discovered([robot_position[0] + 1, robot_position[1]]):
        input_movement = 4
        return
    input_movement = move_robot_to_shortest_dist(robot_position)



while not robot_stop:
    machine.run()
    process_output(machine.output)
    check_robot_finished()
    determine_input()
    print(input_movement)
    machine.set_input(input_movement)
    machine.unpause()

print("walls: " + str(sorted(set_of_walls)))
print("spaces: " + str(sorted(set_of_spaces)))
print("oxygen: " + str(location_of_oxygen))

for i in range(-22,22):
    for j in range(-22,22):
        if j == 21:
            if str([j, i]) in set_of_spaces:
                print(".")
            elif str([j, i]) in set_of_walls:
                print("#")
            elif str([j, i]) == str(location_of_oxygen):
                print("O")
            else:
                print(" ")
        else:
            if str([j, i]) == "[0, 0]":
                print("S", end = "")
            elif str([j, i]) in set_of_spaces:
                print(".", end = "")
            elif str([j, i]) in set_of_walls:
                print("#", end = "")
            elif str([j, i]) == str(location_of_oxygen):
                print("O", end = "")
            else:
                print(" ", end = "")

print("number of moves to oxygen = " + str(distances_from_centre["[-12, 15]"] + 1))
