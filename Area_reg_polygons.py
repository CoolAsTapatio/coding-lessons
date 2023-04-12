# Untitled.py
# Created by Kids on 1/10/23.
import math

class Shape:
	def __init__(self, type_of_shape):
		self.shape_name = type_of_shape
		self.number_of_sides = self.calculate_number_of_sides()
		self.angles = self.set_angle()
		self.area = self.set_area()
	
	def calculate_number_of_sides(self):
		if self.shape_name == "circle":
			return 0
		elif self.shape_name == "square":
			return 4
		elif self.shape_name == "rectangle":
			return 4
		elif self.shape_name == "triangle":
			return 3
		elif self.shape_name == "trapezoid":
			return 4
		elif self.shape_name == "hexagon":
			return 6
		else:
			raise(SyntaxError)
	def set_angle(self):
		if self.number_of_sides ==  0:
			return 360
		return ((self.number_of_sides-2)*180)/self.number_of_sides
	
	def set_area(self):
		if self.shape_name == "circle":
			return get_circle_area()
		elif self.shape_name == "square":
			return get_square_area()
		elif self.shape_name == "rectangle":
			return get_rectangle_area()
		elif self.shape_name == "triangle":
			return get_triangle_area()
		elif self.shape_name == "trapezoid":
			return get_trapezoid_area()
		elif self.shape_name == "hexagon":
			return get_hexagon_area()
			
			

def get_circle_area():
		radius = float(input("what is the radius of your circle: "))
		return math.pi * radius * radius
	
def get_square_area():
	side_length = float(input("what is the side length of your square: "))
	return side_length * side_length
def get_rectangle_area():
	length = float(input("what is the length of your rectangle: "))
	width = float(input("what is the width of your rectangle: "))
	return length * width
def get_triangle_area():
	base = float(input("what is the base of your triangle: "))
	height = float(input("what is the height of your triangle: "))
	return base * height/2
def get_trapezoid_area():
	base2 = float(input("what is the base 1 of your trapezoid: "))
	base1 = float(input("what is the base 2 of your trapezoid: "))
	height = float(input("what is the height of your trapezoid: "))
	return (base1+base2)/2 * height
def get_hexagon_area():
	side_length = float(input("what is the sidelength of your hexagon: "))
	return 3*math.sqrt(3)/2*side_length*side_length

if __name__ == "__main__":
	tri1 = Shape("hexagon")
	print(tri1.area)