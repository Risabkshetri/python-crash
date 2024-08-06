## 1. demostrate the installation process of python IDLE and spider anaconda
## 2. write a program to print simple message of hellow world on the screen
# message = 'Hellow world'
# print(message)
# print(message)
## 3. write a program to callculate area of circle and area of rectangle.
#import math

# radius = float(input("Enter radius of a circle: "))

# area = math.pi * radius ** 2

# print("Area of circle = ", area)

# length = float(input("Enter length of Rectangle : "))
# breath = float(input("Enter the breath of Reactangle : "))
# areaOfReactangle = length * breath
# print(areaOfReactangle)

## 4. write a program to identify the type of a particular vaue stored in a variable
# a = 10
# print(type(a))
 
# b = 10.0
# print(type(b))

# c = True
# print(type(c))

# d = "10"
# print(type(d))

# e = "10.0"
# print(type(e))

# f = 3 + 4j
# print(type(f))
# 5. write a program to input marks of five subjects and calculated the sum, avearage and percentage.

# subjects = ["DEC", "Python", "C programming", "OOP", "Data Structures"]
# marks = []
# total_marks = 0

# for subject in subjects:
#     mark = float(input(f"Enter the marks for {subject}: "))
#     marks.append(mark)
#     total_marks += mark

# average = total_marks / len(subjects)
# percentage = (total_marks / (len(subjects) * 100)) * 100

# print("\nIndividual subject marks:")
# for subject, mark in zip(subjects, marks):
#     print(f"{subject}: {mark}")

# print("\nResults:")
# print(f"Total marks: {total_marks}")
# print(f"Average marks: {average:.2f}")
# print(f"Percentage: {percentage:.2f}%")

## 6. demostrate the usases of all the operators in python
# 6.1. arithmetic operators
print(5 + 2)  # Addition: 7
print(5 - 2)  # Subtraction: 3
print(5 * 2)  # Multiplication: 10
print(5 / 2)  # Division: 2.5
print(5 // 2) # Floor Division: 2
print(5 % 2)  # Modulus: 1
print(5 ** 2) # Exponentiation: 25

# 6.2. comparison operators
print(5 == 2)  # Equal to: False
print(5 != 2)  # Not equal to: True
print(5 > 2)   # Greater than: True
print(5 < 2)   # Less than: False
print(5 >= 2)  # Greater than or equal to: True
print(5 <= 2)  # Less than or equal to: False

# 6.3. logical operators
print(5 and 2)  # Logical AND: 2
print(5 or 2)   # Logical OR: 5
print(not 5)    # Logical NOT: False

# 6.4. assignment operators

x = 5
x += 2  # x = x + 2
print(x)  # 7
x -= 2  # x = x - 2
print(x)  # 5
x *= 2  # x = x * 2
print(x)  # 10
x /= 2  # x = x / 2
print(x)  # 5.0

# 6.5. bitwise operators
print(5 & 3)   # Bitwise AND: 1
print(5 | 3)   # Bitwise OR: 7
print(5 ^ 3)   # Bitwise XOR: 6
print(~5)      # Bitwise NOT: -6
print(5 << 1)  # Left shift: 10
print(5 >> 1)  # Right shift: 2

# 6.6. identity operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is z)     # True
print(x is y)     # False
print(x is not y) # True

# 6.7. membership operators
x = [1, 2, 3]
print(1 in x)  # True
print(4 not in x)  # True
