# Dollarizer
def dollarizer(word):
    return word.replace('s', '$')

# Eurizer
def eurizer(word):
    return word.replace('e', '€')

# Replacer
def replacer(word, char1, char2):
    return word.replace(char1, char2)

# Wonky Text
def wonky_text(word):
    word = dollarizer(word)
    word = eurizer(word)
    return word.replace('l', '£')

# Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

# Age in Days
def age_in_days(age):
    return age * 365

# Simple Interest
def simple_interest(p, r, t):
    return p * r * t

# Plan Finances
def plan_finances(p, r, t, desired_amount):
    si = simple_interest(p, r, t)
    total = p + si
    return total >= desired_amount

# Shapes.py
import math

def rectangle_area(length, width):
    return length * width

def circle_area(radius):
    return math.pi * radius * radius

def triangle_area(base, height):
    return 0.5 * base * height

def square_perimeter(side):
    return 4 * side

def circle_details(radius):
    circumference = 2 * math.pi * radius
    area = circle_area(radius)
    print(f"Circumference: {circumference}")
    print(f"Area: {area}")

def geometry(side_length, radius):
    square_perim = square_perimeter(side_length)
    circle_circumference = 2 * math.pi * radius
    
    if square_perim > circle_circumference:
        print("Square has a larger perimeter.")
    else:
        print("Circle has a larger circumference.")
    
    square_area = side_length * side_length
    circle_area_value = circle_area(radius)
    
    if square_area > circle_area_value:
        print("Square has a larger area.")
    else:
        print("Circle has a larger area.")

# Test outputs
print("Dollarizer:", dollarizer("testcase"))
print("Eurizer:", eurizer("testcase"))
print("Replacer:", replacer("testcase", "t", "#"))
print("Wonky Text:", wonky_text("testcase"))
print("Celsius to Fahrenheit:", celsius_to_fahrenheit(25))
print("Age in Days:", age_in_days(25))
print("Simple Interest:", simple_interest(1000, 0.05, 5))
print("Plan Finances:", plan_finances(1000, 0.05, 5, 2000))
print("\nShapes.py tests:")
circle_details(5)
geometry(10, 5)
