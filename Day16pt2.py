# Looks like this one might be too big to brute force from the outset

import time

# with open("day16Input.txt") as f:
#     file_input = f.readlines()
#
# input_string1 = file_input[0]
# input_string1 = input_string1.strip()

input_string1 = "03036732577212944063491565474664"

input_list = []

input_string = ""

for k in range(10000):
    input_string = input_string + input_string1

length_of_input = len(input_string)

for i in range(length_of_input):
    input_list.append(int(input_string[i]))


print("input list created")
print(length_of_input)
no_of_phases = 0


def do_for_1() -> int:
    global input_list
    outt = 0
    for i in range(0, length_of_input - 2, 4):
        outt = outt + input_list[i] - input_list[i + 2]
        # print("i =" + str(i))

    outt = outt + input_list[-2]
    return int(str(outt)[-1])


while no_of_phases < 100:

    # tic = time.perf_counter()
    output_list = [do_for_1()]
    for pattern_no in range(2, length_of_input + 1):
        base = 1
        i = pattern_no - 1
        out = 0
        while i < length_of_input:
            if (i % pattern_no) - pattern_no + 2 == 0:
                if base == 1:
                    out = out + input_list[i]
                else:
                    out = out - input_list[i]
                base = base * -1
                i = i + pattern_no + 1
            else:
                if base == 1:
                    out = out + input_list[i]
                else:
                    out = out - input_list[i]
                i = i + 1

        output_list.append(int(str(out)[-1]))

    input_list = output_list
    no_of_phases = no_of_phases + 1
    print(no_of_phases)
    # toc = time.perf_counter()
    # print(toc - tic)

print(input_list[0:8])

