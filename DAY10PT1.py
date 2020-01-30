import math

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


for asteroid in asteroids:
    relative_asteroids = []
    for relative in asteroids:
        if relative["id"] == asteroid["id"]:
            continue
        if relative["x"] == asteroid["x"]:
            relative_asteroids.append({
                "gradient": "infinity",
                "x_positive": False,
                "y_positive": relative["y"] - asteroid["y"] > 0,
                "distance": abs(relative["y"] - asteroid["y"])
            })

        elif relative["y"] == asteroid["y"]:
            relative_asteroids.append({
                "gradient": 0,
                "x_positive": relative["x"] - asteroid["x"] > 0,
                "y_positive": False,
                "distance": abs(relative["x"] - asteroid["x"])
            })

        # both different
        else:
            relative_asteroids.append({
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
    left = 0
    right = 0
    up = 0
    down = 0

    for relative_asteroid in relative_asteroids:
        if relative_asteroid["gradient"] == 0:
            if relative_asteroid["x_positive"]:
                right = 1
                continue
            else:
                left = 1
                continue

        if relative_asteroid["gradient"] == "infinity":
            if relative_asteroid["y_positive"]:
                down = 1
                continue
            else:
                up = 1
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

    # the number of asteroids visible from the particular asteroid
    asteroid["num"] = left + right + up + down + len(top_left) + len(top_right) + len(bottom_left) + len(bottom_right)


largest = 0
final_asteroid = 0
for asteroid in asteroids:
    if asteroid["num"] > largest:
        largest = asteroid["num"]
        final_asteroid = asteroid

print("final asteroid ")
print(final_asteroid)

print(largest)
