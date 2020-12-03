import json

data = None

with open('lastest.json') as json_file:
    data = json.load(json_file)

    json_file.close()

dict_of_members = {}
for member in data['members']:
    dict_of_scores = {}
    for day in data['members'][member]['completion_day_level']:
        dict_of_scores[day] = int(data['members'][member]['completion_day_level'][day]['2']['get_star_ts']) - int(data['members'][member]['completion_day_level'][day]['1']['get_star_ts'])

    dict_of_members[data['members'][member]['name']] = dict_of_scores

print(dict_of_members)

for i in range(1,4):
    print(' ')
    print('day ' + str(i))
    day_dict = {}
    for member in dict_of_members.keys():
        if str(i) in dict_of_members[member]:
            day_dict[member] = dict_of_members[member][str(i)]

    for name in dict(sorted(day_dict.items(), key=lambda item: item[1])).keys():
        print(name + ' ' + str(day_dict[name]))



# for member in dict_of_members.keys():
#     print(member)
#     for day in dict_of_members[member].keys():
#
#         print(day + str(dict_of_members[member][day]))
