# # 10. WAP to print the grade of a student 
subjects = ["DSA", "Python", "OOPs", "CLE", "Mathematics", "QAPD", "DEC"]
marks = []
total_marks = 0
for subject in subjects:
    mark = float(input(f"Enter marks of {subject} : "))
    marks.append(mark)
    total_marks += mark

average_marks = total_marks / len(subjects)
percentage = (total_marks / (len(subjects) * 100)) * 100

print("Total Marks: ", total_marks)
print("Average Marks: ", average_marks)
print("Percentage: ", percentage, "%")

while True:
    print("1. Percentage is greater than 90")
    print("2. Percentage is greater than 80")
    print("3. Percentage is greater than 70")
    print("4. Percentage is greater than 60")
    print("5. Percentage is greater than 50")
    print("6. Failed")

    if percentage > 90:
        print("Grade: A+")
    elif percentage > 80:
        print("Grade: A")
    elif percentage > 70:
        print("Grade: B")
    elif percentage > 60:
        print("Grade: C")
    elif percentage > 50:
        print("Grade: D")
    else:
        print("You have failed!")
    
    break  # Exit the loop after printing the grade






 

# WAP to check the wheather give year is leap year or not

# year = int(input("Enter a year: "))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")



# 12. WAP to program to print the multiplication table of a number

# a = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{a} x {i} = {a * i}")

# for i in range(1, 11):
#     if i == 10:
#         print(f"{a} x {i} = {a * i}")
#         break
# for i in range(1, 11):
#     if i == 10:
#         print(f"{a} x {i} = {a * i}")
#         continue
    

# 13 WAP to find the greatest number among three numbers

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a > b and a > c:
#     print(f"{a} is the greatest number")
# elif b > a and b > c:
#     print(f"{b} is the greatest number")
# else:
#     print(f"{c} is the greatest number")

# WAP to calculate sum of n natural number:

# n = int(input("Enter number : "))

# for i in range(1, n):
#     sum += i

