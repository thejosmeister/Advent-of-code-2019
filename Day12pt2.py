# Day 12 part 2
# Find lowest number of iterations needed to get back to same point in each direction
# Then find lcm of all three numbers
# (Unfortunately I did this while at work)
from math import gcd


def find_lowest_iteration(int1: int, int2: int, int3: int, int4: int, coord: str) -> int:
    coords = [int1, int2, int3, int4]

    v1 = [0, 0, 0, 0]

    def num_of_els(num: int, mode: int):
        out = 0
        if mode == 1:
            for c in coords:
                if c > num:
                    out = out + 1
        else:
            for c in coords:
                if c < num:
                    out = out + 1

        return out

    def update_coords():
        for i in range(4):
            v1[i] = v1[i] + num_of_els(coords[i], 1) - num_of_els(coords[i], 0)

        coords[0] = coords[0] + v1[0]
        coords[1] = coords[1] + v1[1]
        coords[2] = coords[2] + v1[2]
        coords[3] = coords[3] + v1[3]

    set_of_states = set()
    set_of_states.add(str(coords[0]) + "," + str(coords[1]) + "," + str(coords[2]) + "," + str(coords[3]) + "," + str(v1[0]) + "," + str(v1[1]) + "," + str(v1[2]) + "," + str(v1[3]))

    halt = False
    intt = 0

    while not halt:
        update_coords()
        intt = intt + 1
        state = str(coords[0]) + "," + str(coords[1]) + "," + str(coords[2]) + "," + str(coords[3]) + "," + str(v1[0]) + "," + str(v1[1]) + "," + str(v1[2]) + "," + str(v1[3])
        # print(state)
        if state in set_of_states:
            print("number of iterations required for particular coord: " + coord + " = " + str(intt))
            halt = True
        else:
            set_of_states.add(state)

    return intt


def lcm(num1: int, num2: int) -> int:
    return abs(num1 * num2) // gcd(num1, num2)


print("answer is: " + str(lcm(lcm(find_lowest_iteration(19, 1, 14, 8, "x"), find_lowest_iteration(-10, 2, -4, 7, "y")), find_lowest_iteration(7, -3, 1, -6, "z"))))

