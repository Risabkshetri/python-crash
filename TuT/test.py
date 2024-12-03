# def pyramid_pattern(n):
#     for i in range(n):
#         print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# n = int(input("Enter the number of rows: "))
# pyramid_pattern(n)

# Users = {
#     "id": 1,
#     "Name": "Rishab",
#     "Age": 18,
#     "Friends": ["Aatif", "Shan", "Saddam"],
# }
# print(type(Users))
# print(Users)
# print(Users["Name"])
# print(Users["Friends"])
# print(type(Users["Friends"]))
# print(Users.keys())
# print(Users.values())
# print(Users.items())
# print(sorted(Users))
# del Users["Age"]
# print(Users)
# print(len(Users))
# print(Users.__len__()) 
# Users.clear()
# del Users


# list 

# mylist = [1, 2, 3, 4, 5]
# print(mylist)

# print(type(mylist))

# mylist.append(6)
# print(mylist)

# mylist.insert(0,0)
# print(mylist)

# mylist.remove(6)
# print(mylist)
# mylist.pop(0)
# print(mylist)
# mylist.clear()
# print(mylist)
# del mylist

# #python tuple

# myTup = (1,1,1)
# print(myTup)


# # python sets

# myset = {2,2,3}
# print(myset)

# swapping two numbers

def swap(a,b):
    b = a + b
    a = b - a
    b = b - a
    return a, b;

print(swap(5,6))