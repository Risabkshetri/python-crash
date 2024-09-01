# # if statement
# x = int(input("Enter a number: "))
# if x<=10:
#     print("x is less than or equal to 10")


# # if else statement
# x = int(input("Enter a number: "))
# if x<=10:
#     print("x is less than or equal to 10")
# else:
#     print("x is greater than 10")

#loop: 1.for loop
Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries row wise:")

# For user input
# A for loop for row entries
for row in range(Row):    
    a = []
    # A for loop for column entries
    for column in range(Column):   
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print()

