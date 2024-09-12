## fun with distionary

dict1 = {}
print(type(dict1))

dict = {"fname": "Rishab", "lname": "kshetri"}
print(dict)
print(dict["fname"] + " " + dict["lname"])

dict["age"] = 18
dict["friends"] = "Aatif", "Shan", "Saddam"

print(dict)
print(type(dict["friends"]))

print(dict.keys())
print(dict.values())
print(dict.items())

print(sorted(dict))
# del dict["age"]
# del dict
dict.clear()
print(dict)
