# Build a dictionary of the patterns first, then multiply by the entries


with open("day16Input.txt") as f:
    file_input = f.readlines()

input_string = file_input[0]
input_string = input_string.strip()
input_list = []
length_of_input = len(input_string)

for i in range(length_of_input):
    input_list.append(int(input_string[i]))

dict_of_patterns = {}

for i in range(1, length_of_input + 1):
    ith_list = []
    base = 1
    for j in range(1, length_of_input + 1):
        if j < i:
            ith_list.append(0)
        else:
            if j % i == 0:
                base = base + 1

            if (base % 4) - 1 == 0:
                ith_list.append(0)
            elif (base % 4) - 2 == 0:
                ith_list.append(1)
            elif (base % 4) - 3 == 0:
                ith_list.append(0)
            elif (base % 4) == 0:
                ith_list.append(-1)

    dict_of_patterns[str(i)] = ith_list

no_of_phases = 0

print(dict_of_patterns["7"])
print(dict_of_patterns["650"])

while no_of_phases < 100:

    output_list = []
    for i in range(length_of_input):
        output = 0
        for j in range(length_of_input):
            # print("i = " + str(i) + " j = " + str(j))
            # print(input_list[j])
            # print(dict_of_patterns[str(i+1)][j])
            output = output + (input_list[j] * dict_of_patterns[str(i+1)][j])

        # print(output)
        output_list.append(int(str(output)[-1]))

    input_list = output_list

    no_of_phases = no_of_phases + 1
    print(no_of_phases)

print(input_list[0:8])
