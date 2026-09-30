# FLOAT DATATYPE ASSIGNMENT
# =========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the area of a circle with radius 5.5
print("SOLVED EXAMPLE:")
print("Calculate the area of a circle with radius 5.5")
import math
radius = 5.5
area = math.pi * radius ** 2
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577
print("Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577")
# Your code here
num1 = 3.14
num2 = 2.718
num3 = 1.618
num4 = 0.577

average = (num1 + num2 + num3 + num4) / 4
print("Average value:", average)
=======================================================================

# Question 2: Convert 98.6 Fahrenheit to Celsius (F = C * 9/5 + 32)
print("\nQuestion 2: Convert 98.6 Fahrenheit to Celsius")
# Your code here
fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5 / 9
print("Celsius:", celsius)
=======================================================================
# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years
print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")
# Your code here
principal = 1000
rate = 5.5
time = 3

amount = principal * (1 + rate / 100) ** time
# print(amount)
compound_interest = amount - principal
print("Compound Interest:", compound_interest)
=======================================================================
# Question 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2
print("\nQuestion 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2")
# Your code here
value_a = 3.5
value_b = 4.2

hypotenuse_value = (value_a**2 + value_b**2) ** 0.5
print("Hypotenuse:", hypotenuse_value)
=======================================================================
# Question 5: Calculate the volume of a sphere with radius 7.8
print("\nQuestion 5: Calculate the volume of a sphere with radius 7.8")
# Your code here
=======================================================================
# Question 6: Round 3.14159 to 3 decimal places
print("\nQuestion 6: Round 3.14159 to 3 decimal places")
# Your code here
number = 3.14159

result = round(number, 3)
print(result)
=======================================================================
# Question 7: Calculate the percentage: 45 out of 67
print("\nQuestion 7: Calculate the percentage: 45 out of 67")
# Your code here
part = 45
total = 67
percentage = (part / total) * 100
print("Percentage:", percentage)
=======================================================================
# Question 8: Find the square root of 23.456
print("\nQuestion 8: Find the square root of 23.456")
# Your code here

number = 23.456
square_root = number ** 0.5
print("Square root:", square_root)
=======================================================================
# Question 9: Calculate the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years
print("\nQuestion 9: Calculate simple interest: Principal=2500, Rate=6.5%, Time=2.5 years")
# Your code here

principal = 2500
rate = 6.5
time = 2.5
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)
=======================================================================
# Question 10: Convert 45.7 degrees to radians
print("\nQuestion 10: Convert 45.7 degrees to radians")
# Your code here 
import math

degrees = 45.7
radians = math.radians(degrees)
print("Radians:", radians)
