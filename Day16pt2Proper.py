# Looks like this one might be too big to brute force from the outset

# 12/2/20
# I am an idiot, I thought I needed to get the first 7 digits of the 100th phase permutation not the initial input!!

# Need to find 5977359 - 5977367th digits of 100th phase. These can be calculated recursively.
# 6500000 - 5977359 = 522641
# 522641 / 650 = 804.06....
# 804 * 650 = 522600 so need the 41 rear most digits of ans on front of 804 lots of the input.




with open("day16Input.txt") as f:
    file_input = f.readlines()

input_string1 = file_input[0]
input_string1 = input_string1.strip()

# input_string1 = "03036732577212944063491565474664"
# input_string = "123456789123456789123456789123456789"

input_list = []

input_string = ""

for k in range(804):
    input_string = input_string + input_string1

input_string = input_string1[-41:] + input_string

length_of_input = len(input_string)

for i in range(length_of_input):
    input_list.append(int(input_string[i]))

# Input has been created so now want to implement a recursion formula to find digits at phase 100.

# Original recursion formula didn't work as I was incorrectly using patterns observed when raising
# the corresponding matrix to the power of 100.
# 2nd attempt using find_digit function also didn't work as I reached recursion limit for python.
# Finally just used the same recursion but with a huge dictionary to hold values which worked.
# This would have taken loads less time if I had read the question properly.


print("input list created")
print(length_of_input)
no_of_phases = 0
dict_of_values = {}

for i in range(length_of_input):
    dict_of_values[str([i, 0])] = input_list[i]

a = length_of_input - 1
last_entry = input_list[a]
for i in range(1, 101):
    dict_of_values[str([a, i])] = last_entry

for i in range(1, 101):
    for j in range(length_of_input-2, -1, -1):
        dict_of_values[str([j, i])] = int(str(dict_of_values[str([j + 1, i])] + dict_of_values[str([j, i - 1])])[-1])


print(dict_of_values['[0, 100]'])
print(dict_of_values['[1, 100]'])
print(dict_of_values['[2, 100]'])
print(dict_of_values['[3, 100]'])
print(dict_of_values['[4, 100]'])
print(dict_of_values['[5, 100]'])
print(dict_of_values['[6, 100]'])
print(dict_of_values['[7, 100]'])



# def find_digit(index: int, power: int) -> int:
#     global input_list
#     global dict_of_values
#     print(str(index) + ", " + str(power))
#     if power == 0:
#         return input_list[index]
#     elif index == length_of_input - 1:
#         return input_list[-1]
#     else:
#         dict_constant = str(index) + "," + str(power)
#         if dict_constant in dict_of_values:
#             return dict_of_values[dict_constant]
#         else:
#             interim = int(str(find_digit(index + 1, power) + find_digit(index, power - 1))[-1])
#             dict_of_values[dict_constant] = interim
#             if power == 100:
#                 if index < 8:
#                     print(interim)
#             return int(str(find_digit(index + 1, power) + find_digit(index, power - 1))[-1])
#
#
# find_digit(0, 1)


# a = find_digit(0, 100)

#
# print(a)


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
