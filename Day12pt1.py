# Day 12, I will attempt to write this at home

class Moon:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.x_velocity = 0
        self.y_velocity = 0
        self.z_velocity = 0
        self.kinetic_energy = abs(x) + abs(y) + abs(z)

    def update_position(self):
        self.x = self.x + self.x_velocity
        self.y = self.y + self.y_velocity
        self.z = self.z + self.z_velocity
        self.update_ke()

    def update_ke(self):
        self.kinetic_energy = (abs(self.x) + abs(self.y) + abs(self.z)) * (abs(self.x_velocity) + abs(self.y_velocity) + abs(self.z_velocity))

    def output_velocity(self):
        return {"x vel": self.x_velocity, "y vel": self.y_velocity, "z vel": self.z_velocity}

    def output_position(self):
        return {"x vel": self.x, "y vel": self.y, "z vel": self.z}


def apply_gravity(moon_a: Moon, moon_b: Moon):
    if moon_a.x < moon_b.x:
        moon_a.x_velocity = moon_a.x_velocity + 1
        moon_b.x_velocity = moon_b.x_velocity - 1
    elif moon_a.x > moon_b.x:
        moon_a.x_velocity = moon_a.x_velocity - 1
        moon_b.x_velocity = moon_b.x_velocity + 1

    if moon_a.y < moon_b.y:
        moon_a.y_velocity = moon_a.y_velocity + 1
        moon_b.y_velocity = moon_b.y_velocity - 1
    elif moon_a.y > moon_b.y:
        moon_a.y_velocity = moon_a.y_velocity - 1
        moon_b.y_velocity = moon_b.y_velocity + 1

    if moon_a.z < moon_b.z:
        moon_a.z_velocity = moon_a.z_velocity + 1
        moon_b.z_velocity = moon_b.z_velocity - 1
    elif moon_a.z > moon_b.z:
        moon_a.z_velocity = moon_a.z_velocity - 1
        moon_b.z_velocity = moon_b.z_velocity + 1


moon1 = Moon(19, -10, 7)
moon2 = Moon(1, 2, -3)
moon3 = Moon(14, -4, 1)
moon4 = Moon(8, 7, -6)

number_of_steps = 1000

i = 1

while i < number_of_steps + 1:

    apply_gravity(moon1, moon2)
    apply_gravity(moon1, moon3)
    apply_gravity(moon1, moon4)
    apply_gravity(moon2, moon3)
    apply_gravity(moon2, moon4)
    apply_gravity(moon3, moon4)
    # print("moon1 vel = " + str(moon1.output_velocity()))
    # print("moon1 pos = " + str(moon1.output_position()))
    # print("moon2 vel = " + str(moon2.output_velocity()))
    # print("moon2 pos = " + str(moon2.output_position()))
    # print("moon3 vel = " + str(moon3.output_velocity()))
    # print("moon3 pos = " + str(moon3.output_position()))
    # print("moon4 vel = " + str(moon4.output_velocity()))
    # print("moon4 pos = " + str(moon4.output_position()))
    moon1.update_position()
    moon2.update_position()
    moon3.update_position()
    moon4.update_position()
    # print(moon1.kinetic_energy + moon2.kinetic_energy + moon3.kinetic_energy + moon4.kinetic_energy)
    i = i + 1

print("total KE after 1000 steps: " + str(moon1.kinetic_energy + moon2.kinetic_energy + moon3.kinetic_energy + moon4.kinetic_energy))
	

