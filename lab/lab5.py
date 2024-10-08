# program to perfrom all operations in dict

# dict1 = {}
# print(type(dict1))

# dict = {"fname": "Rishab", "lname": "kshetri"}
# print(dict)
# print(dict["fname"] + " " + dict["lname"])

# dict["age"] = 18
# dict["friends"] = "Aatif", "Shan", "Saddam"

# print(dict)
# print(type(dict["friends"]))

# print(dict.keys())
# print(dict.values())
# print(dict.items())

# print(sorted(dict))
# # del dict["age"]
# # del dict
# dict.clear()
# print(dict)

# # sum of two numbers using function
# num1 = 10
# num2 = 20
# def sum(a, b):
#     sum = a+b
#     print("sum of two numbers = ", sum)

# sum(num1, num2)


# swapping of two numbers using funtion
# num1 = 10
# num2 = 20
# print("numbers after swaping: ")
# print("num1 = ", num1, "num2 = ", num2)
# def swap(a, b):
#     a = a + b;
#     b = a - b
#     a = a - b;
#     print("numbers after swaping: ")
#     print("num1 = ", a, "num2 = ", b)

# swap(num1, num2)
# calculation of area of circle using function
import math

radius = float(input("Enter radius of a circle: "))

def areaOfCircle(r):
    area = math.pi * r ** 2
    print("Area of circle = ", area)


areaOfCircle(radius)

