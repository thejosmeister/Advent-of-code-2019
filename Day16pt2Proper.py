# Looks like this one might be too big to brute force from the outset

# 12/2/20
# I am an idiot, I thought I needed to get the first 7 digits of the 100th phase permutation not the initial input!!

# Need to find 5977359 - 5977367th digits of 100th phase. These can be calculated recursively.
# 6500000 - 5977359 = 522641
# 522641 / 650 = 804.06....
# 804 * 650 = 522600 so need the 41 rear most digits of ans on front of 804 lots of the input.


import time

with open("day16Input.txt") as f:
    file_input = f.readlines()

input_string1 = file_input[0]
input_string1 = input_string1.strip()

# input_string1 = "03036732577212944063491565474664"
# input_string = "123456789123456789"

input_list = []

input_string = ""

for k in range(804):
    input_string = input_string + input_string1

input_string = input_string1[-41:] + input_string

length_of_input = len(input_string)

for i in range(length_of_input):
    input_list.append(int(input_string[i]))

# input has been created so now want to implement a recursion formula to find digits at phase 100.
print("input list created")
print(length_of_input)
no_of_phases = 0


def find_digit(index: int) -> int:
    global input_list
    output = input_list[index]
    counter = 4 + index
    while counter < length_of_input:
        # if length_of_input - counter < 4:
        #     if (counter - index) % 4 == 2:
        #         counter = counter + 2
        #     else:
        #         output = output + input_list[counter]*5
        #         counter = counter + 1
        # else:
            output = output + input_list[counter]*5
            counter = counter + 4

    return int(str(output)[-1])


a = find_digit(0)
b = find_digit(1)
c = find_digit(2)
d = find_digit(3)
e = find_digit(4)
f = find_digit(5)
g = find_digit(6)
h = find_digit(7)
#
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)


# 85798498 is too high

# phases = 0
# output_list = []
#
# for k in range(length_of_input):
#     output_list.append(0)
#
#
# while phases < 100:
#
#     for i in range(length_of_input):
#         for j in range(i, length_of_input):
#             output_list[i] = output_list[i] + input_list[j]
#         output_list[i] = int(str(output_list[i])[-1])
#
#     for k in range(length_of_input):
#         input_list[k] = output_list[k]
#
#     for k in range(length_of_input):
#         output_list[k] = 0
#     phases = phases + 1
#
# print(input_list)

