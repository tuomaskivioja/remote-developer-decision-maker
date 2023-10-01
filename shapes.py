import math

radius = float(input("Enter the radius of the circle: "))
circle_area = math.pi * radius * radius
print(f"The area of the circle with radius {radius} is: {circle_area:.2f}")

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
triangle_area = 0.5 * base * height
print(f"The area of the triangle with base {base} and height {height} is: {triangle_area:.2f}")

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
rectangle_area = length * breadth
print(f"The area of the rectangle with length {length} and breadth {breadth} is: {rectangle_area:.2f}")
