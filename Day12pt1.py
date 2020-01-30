# Day 12, I will attempt to write this at home

class Moon:
	
	def __init__(self, x, y, z)
		self.x = x
		self.y = y
		self.z = z
		self.x_velocity = 0
		self.y_velocity = 0
		self.z_velocity = 0
		self.kinetic_energy = abs(x) + abs(y) + abs(z)
	
	def update_position(new_x, new_y, new_z)
		self.x = new_x
		self.y = new_y
		self.z = new_z
		self.update_ke()
		
	def update_ke()
		self.kinetic_energy = abs(x) + abs(y) + abs(z) + abs(x_velocity) + abs(y_velocity) + abs(z_velocity)
	
	def update_velocity(new_x, new_y, new_z)
		self.x_velocity = new_x
		self.y_velocity = new_y
		self.z_velocity = new_z
		self.update_ke()
	

