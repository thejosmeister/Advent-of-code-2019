import math


def destroy(set_of: list):
    global index
    elements_to_remove = []

    # only do something if list is non empty
    if len(set_of) > 0:

        for gradient in set_of:
            asters = []

            # find list of asteroids on the same line
            for ast in relative_asteroids:
                if ast["gradient"] == gradient:
                    asters.append(ast)

            # if there is only one on line
            if len(asters) == 1:
                destroyed_asteroids.append({
                    "number": index,
                    "asteroid": asters[0]
                })
                index = index + 1

                relative_asteroids.remove(asters[0])
                elements_to_remove.append(gradient)

            else:
                sorted_asters = sorted(asters, key=lambda astr: astr["distance"])
                destroyed_asteroids.append({
                    "number": index,
                    "asteroid": sorted_asters[0]
                })
                index = index + 1

                relative_asteroids.remove(sorted_asters[0])

        # remove gradients where all asteroids have been destroyed
        for element_to_remove in elements_to_remove:
            set_of.remove(element_to_remove)


def destroy_simple(list_in: list):
    global index
    if len(list_in) > 0:
        destroyed_asteroids.append({
            "number": index,
            "asteroid": list_in[0]
        })
        index = index + 1
        relative_asteroids.remove(list_in[0])
        del list_in[0]


input_string = ".###.###.###.#####.######.##.###..###..#.#...####.###.############.###.####.#########..###..#########.##.###########.#.###.###.######..#.#.#.#.##.###.#.####.#####..#.#.##.############.#######.###..##.###.###.##.##..####..##.####.##########.#######.##.###.##########.##..####.#######.#.#####.##.#.#..############.#######.#.##..#####.#####..######..#####.###.#######.#.############.####.#.#.##########."


asteroids = []
i = 0
ide = 1

for chara in input_string:
    x = i % 20 + 1
    y = math.floor(i / 20) + 1
    if chara == "#":
        asteroids.append({
            "id": ide,
            "x": x,
            "y": y,
            "num": 0
        })
        ide += 1
    i += 1

# the asteroid that we can view the most from
asteroid = {'id': 250, 'x': 9, 'y': 17, 'num': 214}


relative_asteroids = []

# find relative coords of all other asteroids
for relative in asteroids:
    if relative["id"] == asteroid["id"]:
        continue
    if relative["x"] == asteroid["x"]:
        relative_asteroids.append({
            "id": relative["id"],
            "gradient": "infinity",
            "x_positive": False,
            "y_positive": relative["y"] - asteroid["y"] > 0,
            "distance": abs(relative["y"] - asteroid["y"])
        })

    elif relative["y"] == asteroid["y"]:
        relative_asteroids.append({
            "id": relative["id"],
            "gradient": 0,
            "x_positive": relative["x"] - asteroid["x"] > 0,
            "y_positive": False,
            "distance": abs(relative["x"] - asteroid["x"])
        })

    # both different
    else:
        relative_asteroids.append({
            "id": relative["id"],
            "gradient": (relative["y"] - asteroid["y"]) / (relative["x"] - asteroid["x"]),
            "x_positive": relative["x"] - asteroid["x"] > 0,
            "y_positive": relative["y"] - asteroid["y"] > 0,
            "distance": abs(relative["y"] - asteroid["y"]) + abs(relative["x"] - asteroid["x"])
        })

# now we have relative positions for each asteroid we can create a set of gradients for each corner
top_left = set()
top_right = set()
bottom_left = set()
bottom_right = set()
left = []
right = []
up = []
down = []

for relative_asteroid in relative_asteroids:
    if relative_asteroid["gradient"] == 0:
        if relative_asteroid["x_positive"]:
            right.append(relative_asteroid)
            continue
        else:
            left.append(relative_asteroid)
            continue

    if relative_asteroid["gradient"] == "infinity":
        if relative_asteroid["y_positive"]:
            down.append(relative_asteroid)
            continue
        else:
            up.append(relative_asteroid)
            continue

    if relative_asteroid["x_positive"]:
        if relative_asteroid["y_positive"]:
            bottom_right.add(relative_asteroid["gradient"])
            continue
        else:
            top_right.add(relative_asteroid["gradient"])
            continue
    elif relative_asteroid["y_positive"]:
        bottom_left.add(relative_asteroid["gradient"])
        continue
    else:
        top_left.add(relative_asteroid["gradient"])
        continue


destroyed_asteroids = []
index = 1

sorted_up = sorted(up, key=lambda astr: astr["distance"])
sorted_right = sorted(right, key=lambda astr: astr["distance"])
sorted_down = sorted(down, key=lambda astr: astr["distance"])
sorted_left = sorted(left, key=lambda astr: astr["distance"])

while index < 201:
    destroy_simple(sorted_up)

    destroy(sorted(top_right))

    destroy_simple(sorted_right)

    destroy(sorted(bottom_right))

    destroy_simple(sorted_down)

    destroy(sorted(bottom_left))

    destroy_simple(sorted_left)

    destroy(sorted(top_left))


print("200th asteroid to be destroyed is:")
print(asteroids[destroyed_asteroids[199]["asteroid"]["id"]-1])



# print(asteroids)
# print(relative_asteroids)
