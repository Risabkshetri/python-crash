# # demonstrate the various method of list

# list1 = ["rishab", 1, 2, 5, 6, 4, 3]

# print(list1)
# list1.reverse()
# print(list1)

# list1.append("kshetri")
# print(list1)

# list1.insert(1,3)
# print(list1)

# # Tuple
# Tuple1 = (1, 2, 3, 4, 5)
# Tuple2 = (6, 7, 8, 9, 10)

# Tuple3 = Tuple1 + Tuple2
# print(Tuple3)

# Tuple1, Tuple2 = Tuple2, Tuple1
# print(Tuple1)
# print(Tuple2)

# print(max(Tuple3))
# print(min(Tuple3))


# set
set1 = {1, 2, 3, 4, 5, 6}
set2 = {7, 8, 1, 10, 3, 2}

set3 = set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)

set5 = set1.difference(set2)
print(set5)

set6 = set1.symmetric_difference(set2)
print("symetric:", set6)

print(max(set3))
print(min(set3))

set3.add(10)
print(set3)

set3.remove(10)
print(set3)

# dictionary

# dict = {"name": "rishab", "age": 18, "city": "Delhi"}
# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict.items())

# dict["Last_name"] = "kshetri", "Rokaha"
# print(dict)