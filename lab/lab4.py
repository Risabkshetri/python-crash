# WAP to print the fibonacci series in python
a = 0
b = 1
c = 0
num = int(input("Enter number of terms: "))
for i in range(0, num):
    print(c, end = " ")
    a = b
    b = c
    c = a + b
    

# Demonstrate all the method in list 

mylist1 = [3, 4, 5, 6, 2, 3, 4, 5, 6, 7]
mylist2 = [4, 6, 17, 18, 19, 20]
print(type(mylist1))
mylist1.append(11)
print(mylist1)
mylist1.extend(mylist2)
print(mylist1)
mylist1.insert(3, 22)
print(mylist1)
mylist1.remove(22)
print(mylist1)
mylist1.pop(3)
print(mylist1)
mylist1.sort()
print(mylist1)
mylist2.reverse()
print(mylist2)
print(mylist1.count(6))
print(mylist1.index(5))
print(mylist1[2:5])
print(max(mylist1))
print(min(mylist1))
mylist1.clear()
print(mylist1)

# WAP to add sum of all element of list
list = [1, 2, 3, 4, 5]
sum = 0
for i in list:
    sum += i
print(sum)

# WAP to find the sum of all positive number in a list
list = [-1, -2, -3, -4, -5, 5, 4, 3, 2, 1]
sum = 0
for i in list:
    if i > 0:
     sum += i
print(sum)

# Demonstrate various operetions in tuple
Tuple1 = (1, 2, 3, 4, 5)
print(type(Tuple1))
Tuple2 = (6, 7, 8, 9, 10)
print(len(Tuple2))
Tuple3 = Tuple1 + Tuple2
print(Tuple3)
print(Tuple1[2])
print(Tuple1[1:4])
print(max(Tuple1))
print(min(Tuple1))
# travese in tuple
for i in Tuple1:
    print(i, end = ' ')
# WAP to reverse a tuple
Tuple1 = (1, 2, 3, 4, 5)
Tuple1 = Tuple1[::-1]
print(Tuple1)


# WAP to swap two tuple
Tuple1 = (1, 2, 3, 4, 5)
Tuple2 = (6, 7, 8, 9, 10)
Tuple1, Tuple2 = Tuple2, Tuple1
print(Tuple1)
print(Tuple2)

# WAP to conver tuple to list
Tuple1 = (1, 2, 3, 4, 5)
List1 = list(Tuple1)
print(List1)

# WAP to demonstrate the various methods in sets

set1 = {1,2,3,4,5,6}
set2 = {7,8,9,10,11,12}
print(type(set1))
set1.add(7)
print(set1)
set1.remove(5)
print(set1)
set1.pop()
print(set1)
set1.update(set2)
print(set1)
set1.discard(10)
print(set1)
set1.difference_update(set2)
print(set1)
set1.clear()
print(set1)


# Find the missing and additional elements in two sets
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8}

# prints the missing and additional elements in list2 
print("Missing values in second list:", (set1.difference(set2)))
print("Additional values in second list:", (set2.difference(set1)))

# prints the missing and additional elements in set1
print("Missing values in first list:", (set2.difference(set1)))
print("Additional values in first list:", (set1.difference(set2)))


# calculate the sum of items of tuple
Tuple = (1, 2, 3, 4, 5)
sum = 0
for i in Tuple:
    sum += i
print(sum)
# adding tuple to list
List = [1, 2, 3, 4, 5]
Tuple = (6, 7, 8, 9, 10)
List.extend(Tuple)
print(List)