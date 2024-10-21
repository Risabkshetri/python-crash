# demonstrate the various method of list

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


# write a python function to return a list of 10 random numbers
import random
def randomNumbers():
    list = []
    for i in range(10):
        list.append(random.randint(1,100))
    return list
print(randomNumbers())