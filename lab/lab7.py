# python program to define a class person containing name and age as variables and set data, function and display as member functions create object of class, initialize and display details of person.


# class Person:
#     def __init__(self):
#         self.name = ""
#         self.age = 0
    
#     def setData(self, n, a):
#         self.name = n
#         self.age = a
    
#     def display(self):
#         print("Name:", self.name, "Age:", self.age)

# myFriend = Person()

# myFriend.setData("Rishab kshetri", 19)

# myFriend.display()


# python code to demonstrate the all types inherritance in single program
# simple inheritance
# multiple inheritance
# multi-level inheritance

# Simple Inheritance (Single Inheritance)
# class A: 
#     def display_a(self):
#         print("Class A")

# class B(A): 
#     def display_b(self):
#         print("Class B")


# # Multiple Inheritance
# class C:  
#     def display_c(self):
#         print("Class C")

# class D(B, C):  
#     def display_d(self):
#         print("Class D")


# # Multi-level Inheritance
# class E(D):  #
#     def display_e(self):
#         print("Class E")

# # Simple Inheritance
# print("Simple Inheritance Example:")
# b_obj = B()
# b_obj.display_a() 
# b_obj.display_b()  

# # Multiple Inheritance
# print("\nMultiple Inheritance Example:")
# d_obj = D()
# d_obj.display_a()  
# d_obj.display_b()  
# d_obj.display_c()  
# d_obj.display_d()  

# # Multi-level Inheritance
# print("\nMulti-level Inheritance Example:")
# e_obj = E()
# e_obj.display_a()  
# e_obj.display_b()  
# e_obj.display_c()  
# e_obj.display_d()  
# e_obj.display_e()  
