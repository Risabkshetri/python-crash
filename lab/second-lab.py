# 7. demondtrate all the string operarions in the C++ programing.

# 1. contatination

a = 'rishabh'
b = 'khetri'

print(a+b) 

# 2. Repeatiation
print(a*3)

# 3. Indexing
print(a[0])
print(a[1])

# 4. Slicing

print(a[0:2])
print(a[0:3])

# 5. len
print(len(a))

# 6. upper
print(a.upper())

# 7. lower
print(a.lower())

# 8. Capitalize
print(a.capitalize())

# max
print(max(a))

# min
print(min(a))

# count
print(a.count('h'))

# not in
print('h' not in a)

# in
print('h' in a)


## 8. write a program to covert the numbers of days into measures of year week and days

day = int(input("Enter the day: "))

year = day // 365
day = day % 365
week = day // 7
day = day % 7

print(f"year:{year},week:{week} and days:{day}")

## 9. write a program to check whether a number is even or odd

num = int(input("Eneter any number : "))
if(num%2 == 0):
    print("number is even") 

else:
    print("number is odd ")
