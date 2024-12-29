a  = 0
b = 0
c = 1
num = int(input("Enter number of terms: "))
while num > 0:
    print(c, end = " ")
    a = b
    b = c
    c = a + b
    num = num - 1
